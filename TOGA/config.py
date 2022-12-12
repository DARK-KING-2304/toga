import json
import os


def get_user_list(config, key):
    with open('{}/TOGA/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER=True
    URL=False
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY=""
    DEL_CMDS=False
    BAN_STICKER=""
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB=""
    WEBHOOK=False
    BOT_API_URL="5696500136:AAF_i0YIrihTkovpuMUroZLNLnO5S5H90J0"
    #kacrmdi
    WOLVES=[5163444566]
    BOT_ID="5696500136" 
    SQLALCHEMY_DATABASE_URI="postgresql://sogelmru:tW-il5de7jwfw3PN_-ZMG1k7_tTzpJHX@peanut.db.elephantsql.com/sogelmru" 
    JOIN_LOGGER="-1001745971242" 
    API_HASH="c1b434defccacad6063758c9a7d76d5d" 
    INFOPIC=True
    TIGERS=[5163444566]
    API_ID="13849191"
    BL_CHATS=[1]
    DB_URL2="egrrjbpz" 
    TOKEN="5696500136:AAF_i0YIrihTkovpuMUroZLNLnO5S5H90J0"
    DEV_USERS=[5163444566]
    DRAGONS=[5163444566]
    SPAMWATCH_API=""
    WALL_API=""
    DEMONS=[5163444566]
    SUPPORT_CHAT="TogaSupport"
    OWNER_USERNAME="Redeye_ghoul"
    DONATION_LINK="lwdaalay"
    EVENT_LOGS="-1001745971242" 
    OWNER_ID="5122071509" 
    TIME_API_KEY=""
    ERROR_LOGS="-1001745971242" 
    BOT_NAME="AstorTestbot"
    STRICT_GBAN=True
    REDIS_URL="redis://betatoga:Betatoga123+@redis-15793.c241.us-east-1-4.ec2.cloud.redislabs.com:15793"
    UPDATE_CHANNEL="TogaUpdates"
    MONGO_DB_URI="mongodb+srv://betatoga:Betatoga123+@betatoga.rrk13ss.mongodb.net/?retryWrites=true&w=majority"
    BOT_USERNAME="AstorTestbot"
    REM_BG_API_KEY=""
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID="-1001679983263"
    STRICT_GMUTE=False
    SPAMWATCH_API=""
    OWNER_NAME="KACCHAN"
    BANCODES=""
    REPOSITORY="GitHub.com/DARK-KING-2304/Haitham2"
    ARQ_API_KEY=""
    ARQ_API_URL=""
    COTB=""
    SPT_CLIENT_SECRET="914a0ed5a4b34f55bdd4144e21410faf"
    SPT_CLIENT_ID="50d55b24e2454b25800ee7a4de207fc3"
    APP_URL="acutebot/webserver"

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
