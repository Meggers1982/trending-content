// Two independent job slots share this shape: the daily pipeline
// (run_pipeline.py, via app/api/run) and ad-hoc trend scans
// (google_trend_radar.py, via app/api/radar). Kept separate so a scan
// doesn't block on / get blocked by a pipeline run, or vice versa.
function createJobState() {
  const job = {
    running: false,
    mode: null,
    startedAt: null,
    finishedAt: null,
    exitCode: null,
    error: null,
    friendlyError: null,
    resultFile: null,
    logs: []
  };

  function resetJob(mode) {
    job.running = true;
    job.mode = mode;
    job.startedAt = new Date().toISOString();
    job.finishedAt = null;
    job.exitCode = null;
    job.error = null;
    job.friendlyError = null;
    job.resultFile = null;
    job.logs = [];
  }

  function appendLog(chunk) {
    const lines = `${chunk}`.split(/\r?\n/).filter(Boolean);
    job.logs.push(...lines);
    job.logs = job.logs.slice(-120);
  }

  function finishJob(exitCode, error = null, friendlyError = null, extra = {}) {
    job.running = false;
    job.finishedAt = new Date().toISOString();
    job.exitCode = exitCode;
    job.error = error;
    job.friendlyError = friendlyError;
    Object.assign(job, extra);
  }

  return { job, resetJob, appendLog, finishJob };
}

const pipelineJobState = createJobState();
export const pipelineJob = pipelineJobState.job;
export const resetJob = pipelineJobState.resetJob;
export const appendLog = pipelineJobState.appendLog;
export const finishJob = pipelineJobState.finishJob;

const radarJobState = createJobState();
export const radarJob = radarJobState.job;
export const resetRadarJob = radarJobState.resetJob;
export const appendRadarLog = radarJobState.appendLog;
export const finishRadarJob = radarJobState.finishJob;
