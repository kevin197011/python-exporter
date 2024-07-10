# frozen_string_literal: true

task default: %w[push]

task :push do
  system 'git add .'
  system 'git update-index --chmod=+x deploy.sh'
  system "git commit -m 'Update #{Time.now}.'"
  system 'git push origin main'
end
