import ydb

from cars_reader import reader
from dbclient import ydb_client
from serialize import to_json_array
from serialize import is_exist
from exception import ConnectionFailure

import json

pool = ydb.SessionPool(ydb_client.create_driver())

def bad_request(code: int = 400, body = None):
  return {
    'statusCode': code,
    'body': body
  }

def usual_responce(result):
  return {
    'statusCode': 200,
    'body': to_json_array(result[0].rows)
  }

def check(result):
  return is_exist(result[0].rows)

def okey_insert(result):
  return {
    'statusCode': 200,
    'body': "success"
  }

def bad_foreign_key(code: int = 420, body = "no_foreign_key"):
  return {
    'statusCode': code,
    'body': body
  }

def automobile_get_request(parameters):
  if parameters['data'] == 'automobile_list':
    return usual_responce(pool.retry_operation_sync(reader.select_all_cars))
  elif parameters['data'] == 'route_list':
    return usual_responce(pool.retry_operation_sync(reader.select_routes))
  elif parameters['data'] == 'list_by_line':
    reader.set_route(parameters['line'])
    return usual_responce(pool.retry_operation_sync(reader.list_by_lyne))
  elif parameters['data'] == 'delete_troll':
    reader.set_number(parameters['number'])
    return okey_insert(pool.retry_operation_sync(reader.delete_troll))
  elif parameters['data'] == 'delete_route':
    reader.set_route(parameters['line'])
    if (check(pool.retry_operation_sync(reader.is_trolls))==False):
      return okey_insert(pool.retry_operation_sync(reader.delete_route))
    else:
      return bad_foreign_key()
  elif parameters['data'] == 'is_line':
    reader.set_route(parameters['line'])
    return usual_responce(pool.retry_operation_sync(reader.is_lyne))
  elif parameters['data'] == 'is_trolls':
    reader.set_route(parameters['line'])
    return usual_responce(pool.retry_operation_sync(reader.is_trolls))
  else:
    return bad_request('Incorrect query parameters')

def handler(event, context):
  if(event['httpMethod'] == 'GET'):
    return automobile_get_request(event['queryStringParameters'])
  elif(event['httpMethod'] == 'POST'):
    return automobile_post_request(event['queryStringParameters'])
  else:
    return bad_request()
  return {
    'statusCode': 200
  }

def automobile_post_request(parameters):
  if parameters['data'] == 'insert_route':
    reader.set_route(parameters['line'])
    reader.set_start(parameters['start'])
    reader.set_end(parameters['end'])
    reader.set_stops(parameters['stops'])
    return okey_insert(pool.retry_operation_sync(reader.insert_route))
  elif parameters['data'] == 'insert_troll':
    reader.set_number(parameters['number'])
    reader.set_model(parameters['model'])
    reader.set_route(parameters['line'])
    if (check(pool.retry_operation_sync(reader.is_lyne))):
      return okey_insert(pool.retry_operation_sync(reader.insert_troll))
    else:
      return bad_foreign_key()
  else:
    return bad_request('Incorrect body parameters')
