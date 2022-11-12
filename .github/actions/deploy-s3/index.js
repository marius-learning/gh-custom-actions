const core = require("@actions/core");
const exec = require("@actions/exec");
// const github = require("@actions/github");

function run() {
  const bucketName = core.getInput("bucket-name", {
    trimWhitespace: true,
    required: true
  });
  const bucketRegion = core.getInput("bucket-region", {
    required: true,
    trimWhitespace: true
  });
  const appFolder = core.getInput("app-folder", {
    required: true,
    trimWhitespace: true
  });

  exec.exec(
    `aws s3 sync ${appFolder} s3://${bucketName} --delete --region ${bucketRegion}`
  );
}

run();
