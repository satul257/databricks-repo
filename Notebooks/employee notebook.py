# Databricks notebook source
# MAGIC %sql
# MAGIC describe history employee

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse'
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- store version to version 3
# MAGIC select * from employee@v3;
# MAGIC -- anothery way we can write
# MAGIC select * from employee version as of 3
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Optimize command
# MAGIC --optimize employee zorder by (id)
# MAGIC -- try to remove unused files after optimize by default retention period is 7 days and we can not set it to 0 until manually setting changed 
# MAGIC --Vacuum employee retain 0 hours
# MAGIC
# MAGIC -- manually disable retention period (not recommended for production)
# MAGIC set spark.databrick.delta.retentiondurationcheck.enabled =  false;

# COMMAND ----------

# MAGIC %fs ls 
