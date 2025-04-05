{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<mysql.connector.connection_cext.CMySQLConnection object at 0x0000018405237B30>\n"
     ]
    }
   ],
   "source": [
    "connection= mysql.connector.connect(\n",
    " host= \"localhost\",\n",
    " user= \"root\",\n",
    " password=\"4000@Sivaram\",\n",
    " database=\"tourism\"\n",
    " )\n",
    "print(connection)\n",
    "mycursor = connection.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tables in Tourism Projrct\n",
      "city\n",
      "continent\n",
      "country\n",
      "item\n",
      "mode\n",
      "region\n",
      "transaction\n",
      "type\n",
      "user\n"
     ]
    }
   ],
   "source": [
    "mycursor.execute(\"SHOW TABLES\")\n",
    "tables=mycursor.fetchall()\n",
    "\n",
    "print(\"Tables in Tourism Projrct\")\n",
    "for table in tables:\n",
    "    print(table[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 1: Createde table 'Table_1' (transaction + User)\n"
     ]
    }
   ],
   "source": [
    "query_1=\"\"\"create table if not exists Table_1 as\n",
    "select t.TransactionId,t.UserId,t.VisitYear,t.VisitMonth,t.VisitModeId,t.AttractionId,t.Rating,\n",
    "u.ContinentId,u.RegionId,u.CountryId,u.CityId\n",
    "from `transaction` t\n",
    "inner join `User` u \n",
    "on t.UserId=u.UserId;\"\"\"   \n",
    "\n",
    "mycursor.execute(query_1)\n",
    "connection.commit()\n",
    "print(\"Step 1: Createde table 'Table_1' (transaction + User)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 2: Createde table 'Table_2' (Table_1 + Continent)\n"
     ]
    }
   ],
   "source": [
    "query_2=\"\"\"create table if not exists Table_2 as\n",
    "select t1.*,c.Continent\n",
    "from Table_1 t1\n",
    "inner join continent c \n",
    "on t1.ContinentId=c.ContinentId;\"\"\"   \n",
    "\n",
    "mycursor.execute(query_2)\n",
    "connection.commit()\n",
    "print(\"Step 2: Createde table 'Table_2' (Table_1 + Continent)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 3: Createde table 'Table_3' (Table_2 + Region)\n"
     ]
    }
   ],
   "source": [
    "query_3=\"\"\"create table if not exists Table_3 as\n",
    "select t2.*,r.Region\n",
    "from Table_2 t2\n",
    "inner join region r \n",
    "on t2.RegionId=r.RegionId;\"\"\"   \n",
    "\n",
    "mycursor.execute(query_3)\n",
    "connection.commit()\n",
    "print(\"Step 3: Createde table 'Table_3' (Table_2 + Region)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 4: Created table `Table_4` (Table_3 + country)\n"
     ]
    }
   ],
   "source": [
    "query_4 = \"\"\"\n",
    "CREATE TABLE IF NOT EXISTS Table_4 AS\n",
    "SELECT t3.*, co.Country\n",
    "FROM Table_3 t3\n",
    "INNER JOIN country co ON t3.CountryId = co.CountryId;\n",
    "\"\"\"\n",
    "\n",
    "mycursor.execute(query_4)\n",
    "connection.commit()\n",
    "print(\"Step 4: Created table `Table_4` (Table_3 + country)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 5: Created table `Table__5` (Table_4 + city)\n"
     ]
    }
   ],
   "source": [
    "query_5 = \"\"\"\n",
    "CREATE TABLE IF NOT EXISTS Table_5 AS\n",
    "SELECT t4.*, ci.CityName\n",
    "FROM Table_4 t4\n",
    "INNER JOIN city ci ON t4.CityId = ci.CityId;\n",
    "\"\"\"\n",
    "\n",
    "mycursor.execute(query_5)\n",
    "connection.commit()\n",
    "print(\"Step 5: Created table `Table__5` (Table_4 + city)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 6: Created table `Table_6` (Table_5 + item)\n"
     ]
    }
   ],
   "source": [
    "query_6 = \"\"\"\n",
    "CREATE TABLE IF NOT EXISTS Table_6 AS\n",
    "SELECT t5.*, it.Attraction, it.AttractionAddress, it.AttractionTypeId,it.AttractionCityId\n",
    "FROM Table_5 t5\n",
    "INNER JOIN item it ON t5.AttractionId = it.AttractionId;\n",
    "\"\"\"\n",
    "\n",
    "mycursor.execute(query_6)\n",
    "connection.commit()\n",
    "print(\"Step 6: Created table `Table_6` (Table_5 + item)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 7: Created table `Table_7` (Table_6 + type)\n"
     ]
    }
   ],
   "source": [
    "query_7 = \"\"\"\n",
    "CREATE TABLE IF NOT EXISTS Table_7 AS\n",
    "SELECT t6.*, t.AttractionType\n",
    "FROM Table_6 t6\n",
    "INNER JOIN type t ON t6.AttractionTypeId = t.AttractionTypeId;\n",
    "\"\"\"\n",
    "\n",
    "mycursor.execute(query_7)\n",
    "connection.commit()\n",
    "print(\"Step 7: Created table `Table_7` (Table_6 + type)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Step 8: Created table `Final_Table` (Table_7 + mode)\n"
     ]
    }
   ],
   "source": [
    "query_8 = \"\"\"\n",
    "CREATE TABLE IF NOT EXISTS Final_Table AS\n",
    "SELECT t7.*, m.VisitMode AS VisitModeName\n",
    "FROM Table_7 t7\n",
    "INNER JOIN mode m ON t7.VisitModeId = m.VisitModeId;\n",
    "\"\"\"\n",
    "\n",
    "mycursor.execute(query_8)\n",
    "connection.commit()\n",
    "print(\"Step 8: Created table `Final_Table` (Table_7 + mode)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "query_final = \"SELECT * FROM Final_Table;\"\n",
    "mycursor.execute(query_final)\n",
    "result_final = mycursor.fetchall()\n",
    "columns_final = [desc[0] for desc in mycursor.description]\n",
    "\n",
    "df_final = pd.DataFrame(result_final, columns=columns_final)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
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
       "      <th>TransactionId</th>\n",
       "      <th>UserId</th>\n",
       "      <th>VisitYear</th>\n",
       "      <th>VisitMonth</th>\n",
       "      <th>VisitModeId</th>\n",
       "      <th>AttractionId</th>\n",
       "      <th>Rating</th>\n",
       "      <th>ContinentId</th>\n",
       "      <th>RegionId</th>\n",
       "      <th>CountryId</th>\n",
       "      <th>...</th>\n",
       "      <th>Continent</th>\n",
       "      <th>Region</th>\n",
       "      <th>Country</th>\n",
       "      <th>CityName</th>\n",
       "      <th>Attraction</th>\n",
       "      <th>AttractionAddress</th>\n",
       "      <th>AttractionTypeId</th>\n",
       "      <th>AttractionCityId</th>\n",
       "      <th>AttractionType</th>\n",
       "      <th>VisitModeName</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5661</td>\n",
       "      <td>0000000014</td>\n",
       "      <td>2018</td>\n",
       "      <td>12</td>\n",
       "      <td>4</td>\n",
       "      <td>640</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>20</td>\n",
       "      <td>155</td>\n",
       "      <td>...</td>\n",
       "      <td>Europe</td>\n",
       "      <td>Southern Europe</td>\n",
       "      <td>Portugal</td>\n",
       "      <td>Lagos</td>\n",
       "      <td>Sacred Monkey Forest Sanctuary</td>\n",
       "      <td>Jl. Monkey Forest, Ubud 80571 Indonesia</td>\n",
       "      <td>63</td>\n",
       "      <td>1</td>\n",
       "      <td>Nature &amp; Wildlife Areas</td>\n",
       "      <td>Friends</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>67652</td>\n",
       "      <td>0000000014</td>\n",
       "      <td>2018</td>\n",
       "      <td>12</td>\n",
       "      <td>4</td>\n",
       "      <td>748</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>20</td>\n",
       "      <td>155</td>\n",
       "      <td>...</td>\n",
       "      <td>Europe</td>\n",
       "      <td>Southern Europe</td>\n",
       "      <td>Portugal</td>\n",
       "      <td>Lagos</td>\n",
       "      <td>Tegalalang Rice Terrace</td>\n",
       "      <td>Jalan Raya Ceking, Tegalalang 80517 Indonesia</td>\n",
       "      <td>72</td>\n",
       "      <td>1</td>\n",
       "      <td>Points of Interest &amp; Landmarks</td>\n",
       "      <td>Friends</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>68777</td>\n",
       "      <td>0000000014</td>\n",
       "      <td>2018</td>\n",
       "      <td>12</td>\n",
       "      <td>4</td>\n",
       "      <td>748</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>20</td>\n",
       "      <td>155</td>\n",
       "      <td>...</td>\n",
       "      <td>Europe</td>\n",
       "      <td>Southern Europe</td>\n",
       "      <td>Portugal</td>\n",
       "      <td>Lagos</td>\n",
       "      <td>Tegalalang Rice Terrace</td>\n",
       "      <td>Jalan Raya Ceking, Tegalalang 80517 Indonesia</td>\n",
       "      <td>72</td>\n",
       "      <td>1</td>\n",
       "      <td>Points of Interest &amp; Landmarks</td>\n",
       "      <td>Friends</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4735</td>\n",
       "      <td>0000000016</td>\n",
       "      <td>2018</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>640</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>14</td>\n",
       "      <td>101</td>\n",
       "      <td>...</td>\n",
       "      <td>Asia</td>\n",
       "      <td>South East Asia</td>\n",
       "      <td>Indonesia</td>\n",
       "      <td>Jakarta</td>\n",
       "      <td>Sacred Monkey Forest Sanctuary</td>\n",
       "      <td>Jl. Monkey Forest, Ubud 80571 Indonesia</td>\n",
       "      <td>63</td>\n",
       "      <td>1</td>\n",
       "      <td>Nature &amp; Wildlife Areas</td>\n",
       "      <td>Family</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5318</td>\n",
       "      <td>0000000016</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>4</td>\n",
       "      <td>640</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>14</td>\n",
       "      <td>101</td>\n",
       "      <td>...</td>\n",
       "      <td>Asia</td>\n",
       "      <td>South East Asia</td>\n",
       "      <td>Indonesia</td>\n",
       "      <td>Jakarta</td>\n",
       "      <td>Sacred Monkey Forest Sanctuary</td>\n",
       "      <td>Jl. Monkey Forest, Ubud 80571 Indonesia</td>\n",
       "      <td>63</td>\n",
       "      <td>1</td>\n",
       "      <td>Nature &amp; Wildlife Areas</td>\n",
       "      <td>Friends</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   TransactionId      UserId  VisitYear  VisitMonth  VisitModeId  \\\n",
       "0           5661  0000000014       2018          12            4   \n",
       "1          67652  0000000014       2018          12            4   \n",
       "2          68777  0000000014       2018          12            4   \n",
       "3           4735  0000000016       2018           4            3   \n",
       "4           5318  0000000016       2017          12            4   \n",
       "\n",
       "   AttractionId  Rating  ContinentId  RegionId  CountryId  ...  Continent  \\\n",
       "0           640       4            5        20        155  ...     Europe   \n",
       "1           748       5            5        20        155  ...     Europe   \n",
       "2           748       5            5        20        155  ...     Europe   \n",
       "3           640       5            3        14        101  ...       Asia   \n",
       "4           640       5            3        14        101  ...       Asia   \n",
       "\n",
       "            Region    Country CityName                      Attraction  \\\n",
       "0  Southern Europe   Portugal    Lagos  Sacred Monkey Forest Sanctuary   \n",
       "1  Southern Europe   Portugal    Lagos         Tegalalang Rice Terrace   \n",
       "2  Southern Europe   Portugal    Lagos         Tegalalang Rice Terrace   \n",
       "3  South East Asia  Indonesia  Jakarta  Sacred Monkey Forest Sanctuary   \n",
       "4  South East Asia  Indonesia  Jakarta  Sacred Monkey Forest Sanctuary   \n",
       "\n",
       "                               AttractionAddress AttractionTypeId  \\\n",
       "0        Jl. Monkey Forest, Ubud 80571 Indonesia               63   \n",
       "1  Jalan Raya Ceking, Tegalalang 80517 Indonesia               72   \n",
       "2  Jalan Raya Ceking, Tegalalang 80517 Indonesia               72   \n",
       "3        Jl. Monkey Forest, Ubud 80571 Indonesia               63   \n",
       "4        Jl. Monkey Forest, Ubud 80571 Indonesia               63   \n",
       "\n",
       "   AttractionCityId                  AttractionType VisitModeName  \n",
       "0                 1         Nature & Wildlife Areas       Friends  \n",
       "1                 1  Points of Interest & Landmarks       Friends  \n",
       "2                 1  Points of Interest & Landmarks       Friends  \n",
       "3                 1         Nature & Wildlife Areas        Family  \n",
       "4                 1         Nature & Wildlife Areas       Friends  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_final.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Final Combined file has been saved\n"
     ]
    }
   ],
   "source": [
    "df_final.to_csv(\"Final_Tourim_Table.csv\",index=False)\n",
    "print(\"The Final Combined file has been saved\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
