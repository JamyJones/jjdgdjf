USER=xtekky \
REPO=gpt4free \
GITHUB_API="https://api.github.com/repos/${USER}/${REPO}/releases/latest"
LATEST_URL=$(curl -L \
  -H 'Accept: application/json' \
  $GITHUB_API | jq -r ".zipball_url" | sed 's/\"//g')
echo $LATEST_URL
echo "Downloading ..." 

curl -LC - \
 "${LATEST_URL}" -o vid.zip
