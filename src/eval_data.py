#!/usr/bin/env python3
import pandas as pd 
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

class df_data():
  def __init__(self):
    self.gentoo = pd.read_csv('../data/gentoo_bugs_before_2012.csv')
    self.kde = pd.read_csv('../data/kde_bugs_before_2012.csv')
    self.suse = pd.read_csv('../data/suse_bugs_before_2012.csv')

def get_tickets_per_year(df): 
    # Oldest ticket is 1997, latest is 2011   
    full_year_list = [dt.datetime.fromisoformat(d).year for d in df['creation_time']]
    year_list, counts = np.unique(full_year_list, return_counts=True)

  
    return year_list, counts

def create_tickets_per_year_plot(data):
  gentoo_years, gentoo_counts = get_tickets_per_year(data.gentoo)
  kde_years, kde_counts = get_tickets_per_year(data.kde)
  suse_years, suse_counts = get_tickets_per_year(data.suse)  
  
  fig, ax = plt.subplots()
  w = 0.25
  ax.bar(gentoo_years, gentoo_counts, width=w, label='Gentoo')
  ax.bar(kde_years + w, kde_counts, width=w, label='KDE')
  ax.bar(suse_years - w, suse_counts, width=w, label='Suse')  
  ax.set_title('Reports per Year')
  ax.set_xlabel('Year')
  ax.set_ylabel('Report Count')
  ax.legend()
  plt.show()



def main():
  
  data = df_data()

  create_tickets_per_year_plot(data)  

  
if __name__ == '__main__':
  main()