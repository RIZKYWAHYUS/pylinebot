import  requests
import  json
import  os

import  sys
import  logging
import  rds_config
import  pymysql

rds_host  = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
except Exception as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    logger.error("Penyebab ERROR : ")
    logger.error(str(e))
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")

HEADER = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ' + 'GANTI_DENGAN_LINE_ACCESS_TOKEN'
}

def lambda_handler(event, context):

    body = json.loads(event['body'])
    with conn.cursor() as cur:
        for event in body['events']:
    
            payload = {
                'replyToken': event['replyToken'],
                'messages': []
            }
            
    
                    
            if event['message']['type'] == 'text':
                payload['messages'].append({
                    'type': 'text',
                    'text':  event['message']['text']
                })
                
                cur.execute('insert into chat (type_message, reply_token, user_id_sender, timestamp, message_type, message_text) values("'+event['type']+'", "'+event['replyToken']+'", "'+event['source']['userId']+'", "'+str(event['timestamp'])+'", "'+event['message']['type']+'", "'+event['message']['text']+'" )')
                conn.commit()
                    
            elif event['message']['type'] == 'sticker':
                payload['messages'].append({
                    'type': 'sticker',
                    'stickerId': event['message']['stickerId'],
                    'packageId': event['message']['packageId']
                })
            else:
                payload['messages'].append({
                    'type': 'text',
                    'text':  str(event)
                })
    
            if len(payload['messages']) > 0:
                response = requests.post('https://api.line.me/v2/bot/message/reply',
                    headers=HEADER,
                    data=json.dumps(payload))