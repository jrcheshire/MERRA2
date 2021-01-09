#Frequency Step Test
dfList = [100, 1000, 2000, 10000]
m.defineSite(sitestr = "SouthPole")
date = '20150601'
outFile = 'SouthPole_%s_000000_gndData1.out'%date
errFile = 'SouthPole_%s_000000_gndData1.err'%date
f220,band220f,band220rj = m.readBandpass(band='220')
band220rj = band220f  # hack because rj band is missing
f150,band150f,band150rj = m.readBandpass(band='150')
f100,band100f,band100rj = m.readBandpass(band='100')

    #fs, tb, trj, pwv
    plot(a,b, color = 'red')
    plot(a,c, color = 'blue')
    title("Brightness temperature spectrum from am: %s MHz step size"%step)
    show()

    tsky220 = m.integBand(f220,band220rj,b,c)
    tsky150 = m.integBand(f150,band150rj,b,c)
    tsky100 = m.integBand(f100,band100rj,b,c)

scatter(transposed[0],100*(transposed[3]-transposed[3][0])/transposed[3][0])

scatter(transposed[0],100*(transposed[4]-transposed[4][0])/transposed[4][0])

scatter(transposed[0],100*(transposed[5]-transposed[5][0])/transposed[5][0])

scatter(transposed[0], transposed[1])

