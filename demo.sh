#!/usr/bin/env bash
# Demo script for Task Manager API
# Replace HOST and TOKEN with your values before running.

HOST="http://127.0.0.1:8000"    # or https://<yourusername>.pythonanywhere.com
TOKEN="efe62adb67ce930cd58d5bfbf7882b301bdfc26f"  # replace with your token

set -e

echo "Host: $HOST"
echo "Using token: ${TOKEN:0:6}..."

echo "== Create task =="
CREATE_RESP=$(curl -s -X POST \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","priority":"high","due_date":"2025-10-20"}' \
  $HOST/api/tasks/)
echo "$CREATE_RESP" | python -m json.tool || echo "$CREATE_RESP"

TASK_ID=$(echo "$CREATE_RESP" | python -c "import sys,json; print(json.load(sys.stdin).get('id'))")
echo "Created task id: $TASK_ID"

echo "== List tasks =="
curl -s -H "Authorization: Token $TOKEN" $HOST/api/tasks/ | python -m json.tool || true

echo "== Mark complete =="
curl -s -X POST -H "Authorization: Token $TOKEN" $HOST/api/tasks/$TASK_ID/mark_complete/ | python -m json.tool || true

echo "== Attempt to edit completed task (expect failure) =="
curl -s -X PUT \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Try edit when completed"}' \
  $HOST/api/tasks/$TASK_ID/ | python -m json.tool || true

echo "== Mark incomplete =="
curl -s -X POST -H "Authorization: Token $TOKEN" $HOST/api/tasks/$TASK_ID/mark_incomplete/ | python -m json.tool || true

echo "== Edit after marking incomplete (expect success) =="
curl -s -X PUT \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy almond milk","priority":"medium"}' \
  $HOST/api/tasks/$TASK_ID/ | python -m json.tool || true

echo "== Final list =="
curl -s -H "Authorization: Token $TOKEN" $HOST/api/tasks/ | python -m json.tool || true

echo "Demo finished"
