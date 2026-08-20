export function explainRunError(rawError, mode = "full") {
  const text = `${rawError || ""}`;
  const lower = text.toLowerCase();
  const action =
    mode === "prefetch" ? "refresh the radar" :
    mode === "scan" ? "run the trend scan" :
    mode === "track" ? "save this tracked topic" :
    "start a new report";

  if (!text.trim()) {
    return `The app could not ${action}. No error details were returned. Try again, then check the run logs if it fails twice.`;
  }

  if (lower.includes("spawn python enoent") || lower.includes("spawn python3 enoent")) {
    return "The app could not find Python on this machine. Install Python 3, or set PYTHON_BIN in your environment to the Python command/path you use.";
  }

  if (lower.includes("missing dependency") && lower.includes("anthropic")) {
    return "The pipeline is missing the Anthropic Python package. Run `pip install -r requirements.txt`, then try again.";
  }

  if (lower.includes("missing dependency") && lower.includes("python-dotenv")) {
    return "The pipeline is missing the dotenv package that reads your .env file. Run `pip install -r requirements.txt`, then try again.";
  }

  if (lower.includes("anthropic_api_key")) {
    return "The Anthropic API key is missing. Add ANTHROPIC_API_KEY to your environment variables, then run again.";
  }

  if (lower.includes("serpapi_api_key") || lower.includes("serpapi key")) {
    return "The SerpAPI key is missing. Add SERPAPI_API_KEY to your environment variables so the radar can fetch Google News and Trends.";
  }

  if (lower.includes("github_pipeline_token")) {
    return "The Vercel app is missing GITHUB_PIPELINE_TOKEN. Add it in Vercel project environment variables so the button can trigger GitHub Actions.";
  }

  if (lower.includes("workflow dispatch failed") && lower.includes("404")) {
    return "GitHub could not find the workflow. Confirm the repo is Meggers1982/trending-content and the workflow file is .github/workflows/run-pipeline.yml on the main branch.";
  }

  if (lower.includes("bad credentials") || (lower.includes("commit failed") && lower.includes("401"))) {
    return "GITHUB_PIPELINE_TOKEN was rejected outright (expired or revoked), not just under-scoped. Generate a new fine-grained token for Meggers1982/trending-content with \"Actions: Read and write\" AND \"Contents: Read and write\" permissions (both are needed — Actions to trigger runs, Contents to save tracked topics), then update GITHUB_PIPELINE_TOKEN in Vercel.";
  }

  if (lower.includes("workflow dispatch failed") && (lower.includes("401") || lower.includes("403"))) {
    return "GitHub rejected the pipeline token. Create a fine-grained token for Meggers1982/trending-content with \"Actions: Read and write\" AND \"Contents: Read and write\" permissions, then update GITHUB_PIPELINE_TOKEN in Vercel.";
  }

  if (lower.includes("could not resolve host") || lower.includes("network") || lower.includes("timed out")) {
    return "The run could not reach an external service. Check network access, then try again. If this happens during radar refresh, SerpAPI or GitHub may be temporarily slow.";
  }

  if (lower.includes("exited with code")) {
    return "The pipeline started but stopped before finishing. Check the latest log lines below for the specific failed step.";
  }

  return text.length > 220
    ? `The run failed: ${text.slice(0, 220)}...`
    : `The run failed: ${text}`;
}
