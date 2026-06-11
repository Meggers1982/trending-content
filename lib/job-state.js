export const pipelineJob = {
  running: false,
  mode: null,
  startedAt: null,
  finishedAt: null,
  exitCode: null,
  error: null,
  logs: []
};

export function resetJob(mode) {
  pipelineJob.running = true;
  pipelineJob.mode = mode;
  pipelineJob.startedAt = new Date().toISOString();
  pipelineJob.finishedAt = null;
  pipelineJob.exitCode = null;
  pipelineJob.error = null;
  pipelineJob.logs = [];
}

export function appendLog(chunk) {
  const lines = `${chunk}`.split(/\r?\n/).filter(Boolean);
  pipelineJob.logs.push(...lines);
  pipelineJob.logs = pipelineJob.logs.slice(-120);
}

export function finishJob(exitCode, error = null) {
  pipelineJob.running = false;
  pipelineJob.finishedAt = new Date().toISOString();
  pipelineJob.exitCode = exitCode;
  pipelineJob.error = error;
}
