if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/dhanush2bot/nobitha-pro-by-filmyspot-movies-.git /nobitha-pro-by-filmyspot-movies-
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /nobitha-pro-by-filmyspot-movies-
fi
cd /nobitha-pro-by-filmyspot-movies-
pip3 install -U -r requirements.txt
echo "Starting...."
python3 bot.py
