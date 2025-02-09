USER=john4650-hub \
REPO=chatGpt-app \
TAG="797.0.0"
GITHUB_API="https://api.github.com/repos/${USER}/${REPO}/releases/tags/${TAG}"
token="$(cat ../.secrets/git_token)"
echo $token
LATEST_URL=$(curl -L \
  -H 'Accept: application/json' \
  -H "Authorization: Bearer $token"\
  $GITHUB_API | jq -r ".assets[] | .url" | sed 's/\"//g')
echo $LATEST_URL
echo "Downloading ..." 
curl -L \
  -H 'Accept: application/octet-stream'\
  -H "Authorization: Bearer $token"\
  -H "Content-Type: audio/mp3"\
 $LATEST_URL -o "../out_/speech${TAG}.mp3"
