
# coding: utf-8

# ## Importing Data into Your H2O Cluster
# ### Supported File Formats
# http://docs.h2o.ai/h2o/latest-stable/h2o-docs/getting-data-into-h2o.html#

# In[1]:


import h2o
h2o.connect()


# ### Importing Data from Various Data Sources
# * Local File System
# * Remote File
# * S3
# * HDFS
# * JDBC

# #### Get data from local file system and import as h2o dataframe
# * cf) importing multiple files : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-munging/importing-files.html#importing-multiple-files

# In[4]:


airline_data_from_local = "datasets/allyears2k.csv"
airline_local_df = h2o.import_file(airline_data_from_local)


# #### Get data from s3 and import as h2o dataframe

# In[3]:


airline_data_from_s3 = "https://s3.amazonaws.com/h2o-airlines-unpacked/allyears2k.csv"
alrline_s3_df = h2o.import_file(path=airline_data_from_s3)


# #### Get data from HDFS and import as h2o dataframe
# To do this, the h2o cluster should have the HDFS client API. we will provide the tutorial in future

# #### Get data from Alluxio FS and import as h2o dataframe
# we will provide the tutorial in near future

# #### Get data from IBM Swift and import as h2o dataframe
# Not yet considered

# #### Get data from JDBC and import as h2o dataframe
# We will provide the tutorial in near future
