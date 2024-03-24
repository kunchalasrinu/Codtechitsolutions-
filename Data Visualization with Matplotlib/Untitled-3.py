{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b6f8695d-1005-4ce1-9f70-b25c1ed80ef9",
   "metadata": {},
   "source": [
    "Write pandas series code to get output without using dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "38bb4159-c4ca-4509-8799-d14a9758ac75",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0f4451cb-dba3-4ba9-880d-2f04430e870c",
   "metadata": {},
   "outputs": [],
   "source": [
    "list_number=[1,4,9,6,7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ede8d93f-015c-4b64-9d3f-41ecef37c95f",
   "metadata": {},
   "outputs": [],
   "source": [
    "series_1=pd.Series(list_number,index=['a','x','c','2','e'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "19a1c282-0227-4f36-86fd-de3dac58b641",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a    1\n",
      "x    4\n",
      "c    9\n",
      "2    6\n",
      "e    7\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(series_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01c5dcee-3b2e-4167-89d0-c1a6629a1b18",
   "metadata": {},
   "source": [
    "Write pandas Series code to get output using dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "193cc39e-04dc-426d-a8a8-1de81f81f955",
   "metadata": {},
   "outputs": [],
   "source": [
    "data={'Bilal':42,'Ayesha':38,'Hadia':39}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3b4b56dd-4dff-489b-a7fd-d66118ffc392",
   "metadata": {},
   "outputs": [],
   "source": [
    "series_2=pd.Series(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a625947a-f643-42ca-9899-8af000c531ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bilal     42\n",
      "Ayesha    38\n",
      "Hadia     39\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(series_2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de7c7cd3-81b9-4ad6-be73-09c7b2415e01",
   "metadata": {},
   "source": [
    "Write Pandas dataframe code to get output using python dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c0b9dbe9-e713-4c4e-847e-e3d2bd6bde7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_2={'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],\n",
    "        'temperature':[32,35,28,24,32,31],\n",
    "        'windspeed':[6,7,2,7,4,2],\n",
    "        'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "86784cbc-5d0e-4b7f-b509-75fb1285cd89",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame(data_2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "954c3d4e-09b3-46c8-9a67-893e9f152d82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        day  temperature  windspeed  event\n",
      "0  1/1/2017           32          6   Rain\n",
      "1  1/2/2017           35          7  Sunny\n",
      "2  1/3/2017           28          2   Snow\n",
      "3  1/4/2017           24          7   Snow\n",
      "4  1/5/2017           32          4   Rain\n",
      "5  1/6/2017           31          2  Sunny\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7e740d0-486f-4929-bf13-951bca778e99",
   "metadata": {},
   "source": [
    " In extension to above question, you are required to replace index by ['a','b','c','d','e','f']\r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b14154eb-63ef-4a65-b594-b76fbdc6bb48",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_2=pd.DataFrame(data_2,index=['a','b','c','d','e','f'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0c04bbf4-b8eb-4251-be20-d9eebee9b094",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        day  temperature  windspeed  event\n",
      "a  1/1/2017           32          6   Rain\n",
      "b  1/2/2017           35          7  Sunny\n",
      "c  1/3/2017           28          2   Snow\n",
      "d  1/4/2017           24          7   Snow\n",
      "e  1/5/2017           32          4   Rain\n",
      "f  1/6/2017           31          2  Sunny\n"
     ]
    }
   ],
   "source": [
    "print(df_2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47bfc0fc-0977-4a6e-94e3-e08d670b53cb",
   "metadata": {},
   "source": [
    " In extension to above Q.3, calculate mean, miximum and minimum for label “temperature”\r\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "94a1b404-0541-47b9-b542-90cafbbf7ea8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean of temperature column is= 30.333333333333332\n"
     ]
    }
   ],
   "source": [
    "mean_temp=df['temperature'].mean()\n",
    "print(\"Mean of temperature column is=\",mean_temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0c541df1-de72-41b0-b0ab-e133e94987bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum of temperature= 35\n"
     ]
    }
   ],
   "source": [
    "max_temp=df['temperature'].max()\n",
    "print(\"Maximum of temperature=\",max_temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3a1458f9-8e2b-4546-b7d3-a4181134d448",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum of temperature= 24\n"
     ]
    }
   ],
   "source": [
    "min_temp=df['temperature'].min()\n",
    "print(\"Minimum of temperature=\",min_temp)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1c47d74-4cb3-4117-b33d-bc6dfd415b9f",
   "metadata": {},
   "source": [
    " Import CSV ‘people.csv’ in the given folder. Keep in mind the following instructions:\r\n",
    "You’re required to import only specific columns [\"First Name\", \"Sex\", \"Email\", “Phone”, “Job Title”]\r\n",
    "Set the following columns [\"Sex\", \"Job Title\"] as index columns\r\n",
    "Skip following rows [1,5]\r\n",
    "Export the CSV as “NewPeople.csv”\r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "350fac0c-cedb-46db-8cbd-13499a3d3e30",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_csv=pd.read_csv(\"people.csv\",usecols=[\"First Name\", \"Sex\", \"Email\", \"Phone\", \"Job Title\"],skiprows=[1,5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a43c2a24-9df3-4a49-8f6e-785099ca5e1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_csv.set_index([\"Sex\",\"Job Title\"],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "98f999fb-f4eb-4685-a4d7-cd075c3306f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_csv.to_csv(\"NewPeople.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ecc6acc-f6df-4c48-b0ad-3332524de8e4",
   "metadata": {},
   "source": [
    " Import excel sheet ‘SampleWork.xlsx’ in the given folder. Keep in mind the following instructions:\r\n",
    "Import sheet 1\r\n",
    "Import only first and last column from sheet 1\r\n",
    "Skip row 2 while importing the sheet\r\n",
    "Set row 2 as header\r\n",
    "export as new sheet."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "03fda345-c430-477b-a02a-884119ad71d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_3=pd.read_excel(\"SampleWork.xlsx\",sheet_name=\"Sheet1\",usecols=[0,-1],skiprows=[1],header=[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7395221d-b46d-454c-840c-37bd0f09a7c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_3.to_excel(\" new sheet.xlsx\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6801c07-3645-464b-9d02-5b540b6db887",
   "metadata": {},
   "source": [
    " Create the following dataframe as AICP_DF then implement different operations as described below:\r\n",
    "select 'Name', 'Qualification' coloumns and save to df1\r\n",
    "add a new column to AICP_DF “Height” with the following values: [5.1, 6.2, 5.1, 5.2,5.1]\r\n",
    "set column “Name” as the index column.\r\n",
    "retrieve row with index “Hifza”\r\n",
    "retrieve row with index 3\r\n",
    "drop row with index “Bilal”"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "5d0d785a-4a10-4bc7-b20c-3c853f5b873b",
   "metadata": {},
   "outputs": [],
   "source": [
    "AICP_DF={'Name':['Sonia','Bilal','Hifza','Kabir','Jazim'],\n",
    "         'Age':[27,24,22,32,23],\n",
    "         'Address':['Lahore','Karachi','Sialkot','Peshawar','lhr'],\n",
    "         'Qualification':['MSc','MA','MCA','Phd','bsc']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "f7a32523-e93d-4f32-813d-66b40a6857ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_3=pd.DataFrame(AICP_DF)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "958019bf-cd98-4eed-a740-9e8bc5ed1eb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Age   Address Qualification\n",
      "0  Sonia   27    Lahore           MSc\n",
      "1  Bilal   24   Karachi            MA\n",
      "2  Hifza   22   Sialkot           MCA\n",
      "3  Kabir   32  Peshawar           Phd\n",
      "4  Jazim   23       lhr           bsc\n"
     ]
    }
   ],
   "source": [
    "print(data_3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "00986d1a-c958-4ccf-89ce-84a59708bde5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1=data_3[['Name','Qualification']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "a269a8e9-9104-45e9-903b-6d0598e3da9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name Qualification\n",
      "0  Sonia           MSc\n",
      "1  Bilal            MA\n",
      "2  Hifza           MCA\n",
      "3  Kabir           Phd\n",
      "4  Jazim           bsc\n"
     ]
    }
   ],
   "source": [
    "print(df1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "c02e3874-a546-42e4-be93-91ad809a32ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_3['Height']=[5.1,6.2,5.1,5.2,5.1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "a266a7e3-91e5-44d9-8a6f-672945393472",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Age   Address Qualification  Height\n",
      "0  Sonia   27    Lahore           MSc     5.1\n",
      "1  Bilal   24   Karachi            MA     6.2\n",
      "2  Hifza   22   Sialkot           MCA     5.1\n",
      "3  Kabir   32  Peshawar           Phd     5.2\n",
      "4  Jazim   23       lhr           bsc     5.1\n"
     ]
    }
   ],
   "source": [
    "print(data_3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "f90b2422-36a5-4ec5-a712-57a2353a9b03",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_data=data_3.set_index('Name')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "23493226-db3a-479a-a951-12d01036bcaa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Age   Address Qualification  Height\n",
      "Name                                      \n",
      "Sonia   27    Lahore           MSc     5.1\n",
      "Bilal   24   Karachi            MA     6.2\n",
      "Hifza   22   Sialkot           MCA     5.1\n",
      "Kabir   32  Peshawar           Phd     5.2\n",
      "Jazim   23       lhr           bsc     5.1\n"
     ]
    }
   ],
   "source": [
    "print(new_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "c718fac1-440c-4498-9aba-ead8dec37901",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age                    32\n",
       "Address          Peshawar\n",
       "Qualification         Phd\n",
       "Height                5.2\n",
       "Name: Kabir, dtype: object"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " new_data.iloc[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "4e8e3e46-073e-4a57-b64f-acf67b294349",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age                   22\n",
       "Address          Sialkot\n",
       "Qualification        MCA\n",
       "Height               5.1\n",
       "Name: Hifza, dtype: object"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_data.loc[\"Hifza\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "29b79403-57f5-4c13-8e3d-8e8f52bd0c84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Address</th>\n",
       "      <th>Qualification</th>\n",
       "      <th>Height</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Sonia</th>\n",
       "      <td>27</td>\n",
       "      <td>Lahore</td>\n",
       "      <td>MSc</td>\n",
       "      <td>5.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Hifza</th>\n",
       "      <td>22</td>\n",
       "      <td>Sialkot</td>\n",
       "      <td>MCA</td>\n",
       "      <td>5.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kabir</th>\n",
       "      <td>32</td>\n",
       "      <td>Peshawar</td>\n",
       "      <td>Phd</td>\n",
       "      <td>5.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jazim</th>\n",
       "      <td>23</td>\n",
       "      <td>lhr</td>\n",
       "      <td>bsc</td>\n",
       "      <td>5.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Age   Address Qualification  Height\n",
       "Name                                      \n",
       "Sonia   27    Lahore           MSc     5.1\n",
       "Hifza   22   Sialkot           MCA     5.1\n",
       "Kabir   32  Peshawar           Phd     5.2\n",
       "Jazim   23       lhr           bsc     5.1"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_data.drop(\"Bilal\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfca0823-ca5c-4c37-bc51-10196db7b158",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}