# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:15:34 2015
bicubic excep north pol and south pol
@author: caiyunapp
"""
import numpy as np
def bicubic(data,userlocation):
    fac=np.empty([4,4])
    p=np.empty([4,4])
    rel_lat=np.empty([4])
    rel_lon=np.empty([4])
    [ntm,nlat,nlon]=np.shape(data)
    dlat=180.0/nlat
    dlon=360.0/nlon
    idx_lat=int((90-userlocation[0])/dlat)
    idx_lat_true=(90-userlocation[0])/dlat
    rslt=np.empty([ntm])
    if idx_lat==0 or idx_lat>=nlat-3:
        return('God bless You ,Happy daventure!')
    if userlocation[1]>0:
        idx_lon=int(userlocation[1]/dlon)
        idx_lon_true=userlocation[1]/dlon
    else:
        idx_lon=int((360+userlocation[1])/dlon)
        idx_lon_true=(360+userlocation[1])/dlon
    rel_lat=[(idx_lat_true-idx_lat)**t for t in [1,2,3,4]]
    rel_lon=[(idx_lon_true-idx_lon)**t for t in [1,2,3,4]]
    count=0
    while count<ntm-1:
        if idx_lon==0:
            p[:,0]=data[count,nlon-2,idx_lat-1:idx_lat+3]
            p[:,1]=data[count,idx_lon,idx_lat-1:idx_lat+3]
            p[:,2]=data[count,idx_lon+1,idx_lat-1:idx_lat+3]
            p[:,3]=data[count,idx_lon+2,idx_lat-1:idx_lat+3]
        if idx_lon==nlon-2:
            p[:,3]=data[count,1,idx_lat-1:idx_lat+3]
            p[:,2]=data[count,idx_lon+1,idx_lat-1:idx_lat+3]
            p[:,1]=data[count,idx_lon,idx_lat-1:idx_lat+3]
            p[:,0]=data[count,idx_lon-1,idx_lat-1:idx_lat+3]
        if idx_lon==nlon-1:
            p[:,3]=data[count,2,idx_lat-1:idx_lat+3]
            p[:,2]=data[count,1,idx_lat-1:idx_lat+3]
            p[:,1]=data[count,idx_lon,idx_lat-1:idx_lat+3]
            p[:,0]=data[count,idx_lon-1,idx_lat-1:idx_lat+3]
        if idx_lon<nlon-2 and idx_lon>0:
            p[:,3]=data[count,idx_lon+2,idx_lat-1:idx_lat+3]
            p[:,2]=data[count,idx_lon+1,idx_lat-1:idx_lat+3]
            p[:,1]=data[count,idx_lon,idx_lat-1:idx_lat+3]
            p[:,0]=data[count,idx_lon-1,idx_lat-1:idx_lat+3]
        fac[0,0]=p[1,1]
        fac[0,1]=-.5*p[1,0]+.5*p[1,2]
        fac[0,2]= p[1,0]-2.5*p[1,1]+2*p[1,2]-.5*p[1,3]
        fac[0,3] =-.5*p[1,0]+1.5*p[1,1]-1.5*p[1,2]+.5*p[1,3]
        fac[1,0]=-.5*p[0,1]+.5*p[2,1]
        fac[1,1]=.25*p[0,0]-.25*p[0,2]-.25*p[2,0]+.25*p[2,2]
        fac[1,2]=-.5*p[0,0]+1.25*p[0,1]-p[0,2]+.25*p[0,3]+.5*p[2,0]-1.25*p[2,1]+p[2,2]-.25*p[2,3]
        fac[1,3]=.25*p[0,0]-.75*p[0,1]+.75*p[0,2]-.25*p[0,3]-.25*p[2,0]+.75*p[2,1]-.75*p[2,2]+.25*p[2,3]
        fac[2,0]=p[0,1]-2.5*p[1,1]+2*p[2,1]-.5*p[3,1]
        fac[2,1]=-.5*p[0,0]+.5*p[0,2]+1.25*p[1,0]-1.25*p[1,2]-p[2,0]+p[2,2]+.25*p[3,0]-.25*p[3,2]
        fac[2,2]=p[0,0]-2.5*p[0,1]+2*p[0,2]-.5*p[0,3]-2.5*p[1,0]+6.25*p[1,1]-5*p[1,2]+1.25*p[1,3]+2*p[2,0]-5*p[2,1]+4*p[2,2]-p[2,3]-.5*p[3,0]+1.25 * p[3,1]-p[3,2]+.25*p[3,3]
        fac[2,3]=-.5*p[0,0]+1.5*p[0,1]-1.5*p[0,2]+.5*p[0,3]+1.25*p[1,0]-3.75*p[1,1]+3.75*p[1,2]-1.25*p[1,3]-p[2,0]+3*p[2,1]-3*p[2,2]+p[2,3]+.25*p[3,0]-.75*p[3,1]+.75*p[3,2]-.25*p[3,3]
        fac[3,0]=-.5*p[0,1]+1.5*p[1,1]-1.5*p[2,1]+.5*p[3,1]
        fac[3,1]=.25*p[0,0]-.25*p[0,2]-.75*p[1,0]+.75*p[1,2]+.75*p[2,0]-.75*p[2,2]-.25*p[3,0]+.25*p[3,2]
        fac[3,2]=-.5*p[0,0]+1.25*p[0,1]-p[0,2]+.25*p[0,3]+1.5*p[1,0]-3.75*p[1,1]+3*p[1,2]-.75*p[1,3]-1.5*p[2,0]+3.75*p[2,1]-3*p[2,2]+.75*p[2,3]+.5*p[3,0]-1.25*p[3,1]+p[3,2]-.25*p[3,3]
        fac[3,3]=.25*p[0,0]-.75*p[0,1]+.75*p[0,2]-.25*p[0,3]-.75*p[1,0]+2.25*p[1,1]-2.25*p[1,2]+.75*p[1,3]+.75*p[2,0]-2.25*p[2,1]+2.25*p[2,2]-.75*p[2,3]-.25*p[3,0]+.75*p[3,1]-.75*p[3,2]+.25*p[3,3]
        rslt[count]=np.dot(np.dot(fac,rel_lon),rel_lat)
        count=count+1
    return rslt
