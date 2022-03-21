import base64
import requests

url = "https://testdocker.modak.com:8888/fireshots/nabu/upd/sq/manageDataMovement/updateSource"
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJhdXRoZW50aWNhdGlvbl9zZXJ2aWNlIjoibGRhcCIsInJvbGVzIjoiV3lCN0lDSnVZV0oxWDNKdmJHVnpJaUE2SUZzZ2V5QWlSbWxzZEdWeUlpQTZJSHNnSW0xdlpHbG1lU0lnT2lCMGNuVmxMQ0FpZG1sbGR5SWdPaUIwY25WbExDQWlZM0psWVhSbElpQTZJSFJ5ZFdVZ2ZTQjlMQ0I3SUNKRmJuUnBkSGtpSURvZ2V5QWliVzlrYVdaNUlpQTZJSFJ5ZFdVc0lDSjJhV1YzSWlBNklIUnlkV1VzSUNKamNtVmhkR1VpSURvZ2RISjFaU0I5SUgwc0lIc2dJazFoYm1GblpTQkJZMk5sYzNNaUlEb2dleUFpYlc5a2FXWjVJaUE2SUhSeWRXVXNJQ0oyYVdWM0lpQTZJSFJ5ZFdVc0lDSmpjbVZoZEdVaUlEb2dkSEoxWlNCOUlIMHNJSHNnSWsxdmJtbDBiM0pwYm1jZ1JHRnphR0p2WVhKa0lpQTZJSHNnSW0xdlpHbG1lU0lnT2lCbVlXeHpaU3dnSW5acFpYY2lJRG9nZEhKMVpTd2dJbU55WldGMFpTSWdPaUJtWVd4elpTQjlJSDBzSUhzZ0lrVjRaV04xZEdsMlpTQkVZWE5vWW05aGNtUWlJRG9nZXlBaWJXOWthV1o1SWlBNklHWmhiSE5sTENBaWRtbGxkeUlnT2lCMGNuVmxMQ0FpWTNKbFlYUmxJaUE2SUdaaGJITmxJSDBnZlN3Z2V5QWlUV0Z1WVdkbElGQnBjR1ZzYVc1bGN5SWdPaUI3SUNKdGIyUnBabmtpSURvZ2RISjFaU3dnSW5acFpYY2lJRG9nZEhKMVpTd2dJbU55WldGMFpTSWdPaUIwY25WbElIMGdmU3dnZXlBaVJHRjBZWE4wYjNKbGN5SWdPaUI3SUNKdGIyUnBabmtpSURvZ2RISjFaU3dnSW5acFpYY2lJRG9nZEhKMVpTd2dJbU55WldGMFpTSWdPaUIwY25WbElIMGdmU3dnZXlBaVEzSmxaR1Z1ZEdsaGJITWlJRG9nZXlBaWJXOWthV1o1SWlBNklIUnlkV1VzSUNKMmFXVjNJaUE2SUhSeWRXVXNJQ0pqY21WaGRHVWlJRG9nZEhKMVpTQjlJSDBzSUhzZ0lrWmhZMlYwSWlBNklIc2dJbTF2WkdsbWVTSWdPaUIwY25WbExDQWlkbWxsZHlJZ09pQjBjblZsTENBaVkzSmxZWFJsSWlBNklIUnlkV1VnZlNCOUxDQjdJQ0pEYjIxd2RYUmxJRVZ1WjJsdVpTSWdPaUI3SUNKdGIyUnBabmtpSURvZ2RISjFaU3dnSW5acFpYY2lJRG9nZEhKMVpTd2dJbU55WldGMFpTSWdPaUIwY25WbElIMGdmU3dnZXlBaVUzbHViMjU1YlNJZ09pQjdJQ0p0YjJScFpua2lJRG9nZEhKMVpTd2dJblpwWlhjaUlEb2dkSEoxWlN3Z0ltTnlaV0YwWlNJZ09pQjBjblZsSUgwZ2ZTd2dleUFpUkdGMFlTQkRiMjV1WldOMGFXOXVjeUlnT2lCN0lDSnRiMlJwWm5raUlEb2dkSEoxWlN3Z0luWnBaWGNpSURvZ2RISjFaU3dnSW1OeVpXRjBaU0lnT2lCMGNuVmxJSDBnZlN3Z2V5QWlSbWxsYkdSemRHOXlaU0lnT2lCN0lDSnRiMlJwWm5raUlEb2dkSEoxWlN3Z0luWnBaWGNpSURvZ2RISjFaU3dnSW1OeVpXRjBaU0lnT2lCMGNuVmxJSDBnZlNCZElIMGdYUT09IiwiaXNzIjoiRklSRVNIT1RTX0FQUExJQ0FUSU9OIiwiZ3JvdXBzIjpbXSwic2Vzc2lvbl9pZCI6MTQ4NjkxMDIsInRpbWVab25lIjoiQXNpYS9Lb2xrYXRhIiwiZXhwIjoxNjQ1NjA4Mzk2LCJ1c2VySWQiOiJSSzA2MDEifQ.iK-8yL493--uyRGr-Mg9XGDU28izAuiw9w6rU455BL-efoGVQ3gqByzpbes4GURH8m1GOiGh42VusEdN1PBZxpEkOxX9yeNM6BsK21GmJzX0G1yYFqdNxA8mfAb0TLavyUjdTJP9MAK9OW3BdFfaEun_LJhjmAi_BXZOH_lfYUSlvNtVVoUiSZE99gnBrs6n-kQGG1jS7WyCImTN-u5hdbtnUUJhwzXtO7Yw8l-6AzG9q5NBS9ezYeLbFcwUHdlSI1AiHnqloboMsyf1AGA1W37ZA8iGi4eAF1SUuG30z8z4hDnnFzXWPoL87xd0T43WPflKE6aWSbrpUhS_fOJf4Q',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Access-Control-Allow-Origin': '*',
  'Cache-Control': 'no-cache, no-store, must-revalidate',
  'Content-Type': 'text/plain'
}

pipeline_names = ["schedule_ssu_inbound_Final_test1"]
sparkconfiguration = []
for i in range(len(pipeline_names)):
    sparkconfiguration.append(
        f"""--master yarn \\
--name "{pipeline_names[i][9:]}" \\
--packages "com.github.music-of-the-ainur:almaren-framework_2.11:0.9.1-2.4,com.github.music-of-the-ainur:http-almaren_2.11:1.2.0-2.4,com.typesafe:config:1.4.0,com.github.music-of-the-ainur:jdbc-almaren_2.11:0.0.1-2.4" \\
--conf spark.dynamicAllocation.enabled=false \\
--conf spark.sql.shuffle.partitions=10 \\
--conf spark.driver.args="{pipeline_names[i][21:]}"  \\
--conf spark.ui.enabled=false \\
--conf spark.ui.retainedStages=100 \\
--conf spark.ui.retainedJobs=100 \\
--conf spark.ui.retainedTasks=100 \\
--conf spark.kryoserializer.buffer.max=2040m \\
--conf spark.sql.shuffle.partitions=20 \\
--conf spark.driver.extraClassPath=code/email_templates/:code/inbound/files/{pipeline_names[i][21:]}/ \\
--conf spark.dynamicAllocation.enabled=false \\
--conf spark.driver.application_status_api_url="https://int-eng-master0.pharma-i.ogvl-eppk.cloudera.site/int-eng/cdp-proxy-api/resourcemanager/v1/cluster/apps" \\
--conf spark.driver.oracle_cred="9,1" \\
--conf spark.driver.vault_cred="10,1" \\
--conf spark.driver.workload_cred="1,1" \\
--conf spark.driver.vault_base_url="https://abbviesbx-etmf-integration-am.veevavault.com" \\
--conf spark.driver.jdbc_url="jdbc:oracle:thin:@UQ00527D.ABBVIENET.COM:1521:ECDPUVT1" \\
--conf "spark.executor.extraJavaOptions=-Dlog4j.configuration=logs.properties" \\
--driver-memory 2G \\
--executor-cores 2 \\
--num-executors 5 \\
--executor-memory 5G \\
--jars $NABU_SPARK_BOT_HOME/jars/nabu-sparkbot-lib-common-assembly-0.8.6.jar,libs/ojdbc6.jar,libs/nabu-sparkbot-lib-common-assembly-0.8.2-SNAPSHOT.jar \\
--driver-java-options '-Dlog4j.configurationFile=logs.properties' \\
--files libs/log4j.properties \\"""
    )

Encoded_Spark_Conf = []
for i in range(len(pipeline_names)):
    Encoded_Spark_Conf.append(str(base64.b64encode(sparkconfiguration[i].encode("ascii")))[2:-1])

a = []
for i in range(len(pipeline_names)):
    a.append("""{
  "data_movement_name": "%s",
  "contact_info": {
    "owner": "RK0601",
    "role": "admin",
    "email": "",
    "description": ""
  },
  "connection_type": "almaren",
  "source_ingestion_details": [
    {
      "dataplace_id": 279,
      "ingest_all_tables_views": [],
      "total_count": 1,
      "schema_id": 59,
      "filters_list": [
        {
          "filter_type_id": 6,
          "filter_value": [],
          "filter_type": "None",
          "priority_order": 1
        }
      ],
      "schema_name": "Pipeline",
      "dataplace_name": "Almaren Curation",
      "root_location_path": null
    }
  ],
  "destination_dataplace_id": 279,
  "destination_dataplace_name": "Almaren Curation",
  "destination_schema_name": "Pipeline",
  "workflow_engine_id": 1,
  "destination_type": "almaren",
  "source_type": "almaren",
  "bot_priority": "Default",
  "compute_engine_id": 100,
  "flow_details": {
    "email_notification": {
      "on_success": [],
      "on_failure": [],
      "email_check": false
    },
    "destination_file_format": "",
    "parallel_source_connections": 3,
    "retry_count": 3,
    "pipeline_retry": false,
    "pipeline_flow_timeout": 7,
    "schema_drift": {
      "enabled": false,
      "email_ids": [],
      "advanced_options_sub_type": "",
      "config": {
        "suffix": "",
        "timestamp": ""
      }
    },
    "inconsistent_data_types": [],
    "unsupported_data_types": {
      "null": [],
      "ignore": [],
      "asis": [],
      "customtext": []
    },
    "ignore_data_types": [],
    "pre_conditions": {
      "enabled": false,
      "pipeline_timeout": 8,
      "pipeline_details": []
    },
    "skip_verification": true,
    "verification_threshold": "",
    "spark_config": {
      "spark_kerberos_command_options": "LS1jb25mIHNwYXJrLnlhcm4ua2V5dGFiPSROQUJVX1NQQVJLX0NVUkFUSU9OX0tFWVRBQl9QQVRIIFwNCi0tY29uZiBzcGFyay55YXJuLnByaW5jaXBhbD0kTkFCVV9TUEFSS19DVVJBVElPTl9QUklOQ0lQQUwgXA",
      "spark_bots_token_command_options": "LS1jb25mIHNwYXJrLm5hYnUudG9rZW49PCVib3RzX3Rva2VuJT4",
      "spark_default_command_options": "%s"
    },
    "git_info": {
      "git_url": "https://github.com/abbvie-internal/ECDP_SSU.git",
      "project_name": "ECDP_SSU",
      "git_branch_or_tag": "main",
      "git_file_path": "code/inbound/ingestionInboundCredentials.scala"
    }
  },
  "destination_schema_id": 59,
  "refresh_freq": {
    "consider_timezone": false,
    "cron_freq": "0 11 13 21 2 ? 2022",
    "cron_timezone": "Asia/Calcutta",
    "cron_type": "one_time"
  },
  "tags": [],
  "data_movement_id": 991,
  "contact_info.description": ""
}"""%(pipeline_names[i], Encoded_Spark_Conf[i]))


for i in range(len(pipeline_names)):
    response = requests.request("POST", url, headers=headers, data=a[i])
    print(response.text)


