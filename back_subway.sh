cd /Users/patch/Documents/project/db/bk
DATE=`date +%Y-%m-%d_%H_%M_%S`
FILENAME2="backup_subway_${DATE}"
mongodump -d subway -o ./
zip ./"${FILENAME2}.zip" -r  ./subway
rm -rf ./subway
