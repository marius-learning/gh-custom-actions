import core from "@actions/core";
import exec from "@actions/exec";

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

  core.setOutput("website-url", `http://${bucketName}`);
}

run();
