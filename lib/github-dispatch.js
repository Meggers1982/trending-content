// Vercel's filesystem has no Python and no SerpAPI key, so anything that needs
// to actually run the pipeline there dispatches a GitHub Actions workflow
// instead, which commits its artifacts back and triggers a fresh deploy.
// app/api/run and app/api/tracked-topics/[id]/scan each had their own copy of
// this; /api/radar would have been the third.

const REPO = process.env.GITHUB_REPOSITORY || "Meggers1982/trending-content";

export function shouldUseGithubActions() {
  return Boolean(process.env.VERCEL || process.env.GITHUB_PIPELINE_TOKEN);
}

export async function triggerGithubWorkflow(workflowId, inputs = {}) {
  const token = process.env.GITHUB_PIPELINE_TOKEN;
  if (!token) {
    return {
      ok: false,
      status: 500,
      message: "GITHUB_PIPELINE_TOKEN is not configured in Vercel."
    };
  }

  const response = await fetch(
    `https://api.github.com/repos/${REPO}/actions/workflows/${workflowId}/dispatches`,
    {
      method: "POST",
      headers: {
        accept: "application/vnd.github+json",
        authorization: `Bearer ${token}`,
        "content-type": "application/json",
        "x-github-api-version": "2022-11-28"
      },
      body: JSON.stringify({
        ref: process.env.GITHUB_PIPELINE_REF || "main",
        inputs
      })
    }
  );

  if (!response.ok) {
    const detail = await response.text();
    return {
      ok: false,
      status: response.status,
      message: `GitHub workflow dispatch failed: ${detail}`
    };
  }

  return { ok: true };
}
