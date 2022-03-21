import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def create_pipelines(baseurl, user, pas, pipelinenames, giturl, projectname, gitbranch, filepath, computeengine, workflowengine, sparkconfiguration ):

    driver = webdriver.Chrome("C:/Users/rk0601/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get(f"{baseurl}/login")
    print(driver.title)
    time.sleep(5)
    username = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/form/div[1]/div/div/input")
    username.send_keys(user)

    time.sleep(5)
    password = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/form/div[2]/div/div/input")
    password.send_keys(pas)

    time.sleep(5)
    password.send_keys(Keys.RETURN)

    for i in range(len(pipelinenames)):
        time.sleep(5)
        driver.get(f"{baseurl}/ingestion/")

        time.sleep(3)
        driver.get(f"{baseurl}/ingestion/almaren")

        time.sleep(3)
        pipeline_name = driver.find_element_by_class_name("ivu-input")
        pipeline_name.send_keys(pipelinenames[i])

        time.sleep(3)
        next_button = driver.find_element_by_id("next-button")
        next_button.click()

        time.sleep(5)
        git_url = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/div/div/input")
        git_url.send_keys(giturl)

        time.sleep(3)
        project_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[1]/div[2]/div/div/div/input")
        project_name.send_keys(projectname)

        time.sleep(3)
        git_branch = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[1]/div/div/div/input")
        git_branch.send_keys(gitbranch)

        time.sleep(3)
        file_path = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/div/div/input")
        file_path.send_keys(filepath)

        time.sleep(3)
        compute_engine = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/div/div/div/div/div/div/input")
        compute_engine.send_keys(computeengine)
        time.sleep(3)
        compute_engine.click()

        time.sleep(5)
        c = driver.find_element_by_xpath(f"//span[contains(@title, '{computeengine}')]")
        time.sleep(5)
        c.click()

        workflow_engine = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/div/input")
        workflow_engine.send_keys(workflowengine)
        time.sleep(3)
        workflow_engine.click()
        time.sleep(5)
        w = driver.find_element_by_xpath(f"//span[contains(@title, '{workflowengine}')]")
        time.sleep(5)
        w.click()
        time.sleep(5)
        next_button1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/span/button")
        next_button1.click()

        time.sleep(5)
        spark_c = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[3]/div/div[1]/div/i")
        spark_c.click()
        time.sleep(5)
        spark_configuration = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[3]/div/div[2]/div/form/div/div/div/textarea")
        spark_configuration.clear()
        spark_configuration.send_keys(sparkconfiguration)

        time.sleep(3)
        next_button2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/span/button")
        next_button2.click()

        time.sleep(3)
        next_button3 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/span/button")
        next_button3.click()

        time.sleep(3)
        schedule = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[4]/form/div/div[2]/div/div/button")
        schedule.click()

        time.sleep(3)
        save = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div/div[5]/button[2]/span")
        save.click()

        time.sleep(3)
        #create = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/span/button")
        #create.click()


baseurl = "https://testdocker.modak.com:8125"
user = "rk0601"
pas = "D8cwHfA5"
pipeline_names = ["schedule_ssu_inbound_sit_1"]
giturl = "https://github.com/abbvie-internal/ECDP_SSU.git"
projectname = "ECDP_SSU"
gitbranch = "main"
filepath = "code/inbound/ingestionInboundCredentials.scala"
computeengine = "test_SACE"
workflowengine = "ingestion_workflow_engine"
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

create_pipelines(baseurl, user, pas, pipeline_names, giturl, projectname, gitbranch, filepath, computeengine, workflowengine, sparkconfiguration)
