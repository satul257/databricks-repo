# Databricks notebook source
# MAGIC %sql
# MAGIC describe history employee

# COMMAND ----------

# MAGIC %fs head dbfs:/user/hive/warehouse/employee/_delta_log/00000000000000000002.json
