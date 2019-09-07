      PROGRAM RDF
      implicit none
      integer i,j,ip,Npmax,Np,nstep,maxbin,bin,Np_A,Np_B,jp,nn,Np_AB
      integer b_in,b_out,b_tot
      parameter(Npmax = 2000000,Np_AB =16962)  ! from 1 to Np_AB to caculate the center of mass 
      parameter(maxbin =160)
      
      character n_flag(npmax),aa,bb
      double precision
     +   rX(Npmax),rY(Npmax),rZ(Npmax), rXc, rYc,
     +   rZc,rXij,rYij,rZij,rijSQ,rij,pi,const,
     +   delr,rho,nid, g(maxbin),
     +   dLx,dLy,dLz,dLxINV,dLyINV,dLzINV,
     +   rlower,rupper,dNp,r,dNp_A,dNp_B,gg(maxbin),
     +   gA(maxbin), gW(maxbin), gC(maxbin),gD(maxbin), gE(maxbin)

      parameter(rho = 3.d0)
    

       open (50,status = 'unknown',
     +       file = 'o-c.dat')

       open (60,status = 'old',
     +       file = 'vesicle.xyz',  ! the input file.xyz
     +       form = 'formatted',
     +       access = 'sequential')

       dLx = 40   ! the box size
       dLy = 40
       dLz = 40

       b_in = 0
       b_out = 0 
       b_tot = 0
  
       rxc = 0.d0
       ryc = 0.d0
       rzc = 0.d0
             
       delr = dLx/maxbin

       do bin = 1,maxbin
          gA(bin) = 0.d0
          gC(bin) = 0.d0
          gW(bin) = 0.d0
          gD(bin) = 0.d0
          gE(bin) = 0.d0
       enddo
      
       read(60,*) np
       read(60,*)
       do ip = 1,np
          read(60,*) n_flag(ip),rX(ip),rY(ip),rZ(ip)
          if(ip.le.NP_AB)then
             rxc = rxc + rX(ip)
             ryc = ryc + rY(ip)
             rzc = rzc + rZ(ip)
          endif
       enddo
       rxc = rxc/NP_AB
       ryc = ryc/NP_AB
       rzc = rzc/NP_AB
       
       do ip = 1,np          
          rXij = rX(ip)-rXc
          rYij = rY(ip)-rYc
          rZij = rZ(ip)-rZc
          rijSQ = rXij*rXij + rYij*rYij + rZij*rZij
          rij = sqrt(rijSQ)
          bin = int(rij/delr)+1
             
       
          if (bin.le.maxbin) then  ! distinguish the type of particles
             if (n_flag(ip).eq.'O') then
                gA(bin) = gA(bin) + 1.d0
             elseif (n_flag(ip).eq.'C')then 
                gC(bin) = gC(bin) + 1.d0
             endif
          endif
       enddo
       
       pi = 4.d0*atan(1.0)
       const = 4.0 * pi/3.0    
       do bin=1,maxbin
          rlower = dble(bin-1)*delr  ! the inner radius 
          rupper = rlower + delr      ! the outer radius
          r = rlower + 0.5*delr       ! make the middle of the thin layer as the coordinate
          
          nid = const*(rupper**3-rlower**3)
          
          gA(bin) = gA(bin)/nid
          gC(bin) = gC(bin)/nid
          write(50,555) r,gA(bin)/3,gC(bin)/3    
       enddo 
              
       call flush(50)
     
 555      format(6(f10.6,5x))  
 556      format(3(i6,3x),f5.2)
       
       write(*,*) 'haha!'
       END
 
