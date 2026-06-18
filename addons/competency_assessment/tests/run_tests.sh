#!/bin/bash
# Automated test runner for Competency Assessment module
# Stops Odoo, runs tests in a clean container, restarts Odoo
set -e

MODULE="competency_assessment"
ODOO_IMAGE="odoo:19.0"
ADDONS="/opt/odoo/addons"
DB_NAME="odoo"
DB_HOST="127.0.0.1"
DB_PORT="5432"
DB_USER="odoo"
DB_PASS="d4cb13a8d80d11b5ae766f7b5b9ce273"
CONTAINER="odoo"

echo "=== Stopping Odoo ==="
docker stop $CONTAINER 2>/dev/null || true

echo "=== Running tests ==="
docker run --rm --network=host \
  --mount type=bind,source=$ADDONS,target=/mnt/extra-addons \
  -e PGHOST=$DB_HOST -e PGPORT=$DB_PORT -e PGUSER=$DB_USER -e PGPASSWORD=*** \
  $ODOO_IMAGE \
  odoo -d $DB_NAME \
    --db_host $DB_HOST --db_port $DB_PORT --db_user $DB_USER --db_password "$DB_PASS" \
    --test-enable -u $MODULE --stop-after-init \
    2>&1 | tee /tmp/odoo_test_output.log

echo ""
echo "=== Test Results ==="
grep -E "FAIL|ERROR|[0-9]+ ok|[0-9]+ failed|[0-9]+ tests" /tmp/odoo_test_output.log || echo "See full log at /tmp/odoo_test_output.log"

echo ""
echo "=== Restarting Odoo ==="
docker start $CONTAINER
sleep 5
echo "Odoo restarted."
