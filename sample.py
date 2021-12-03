import controller as c

c.setIP('192.168.178.25')
c.setGame('pokemon-sword')
c.setController('pro')

c.connect('Sample')

c.click('Y')
c.wait(1)

c.click('DOWN')
c.wait(1)

c.click('A')
c.wait(1)

c.click('A')
c.wait(1)

c.click('A')
c.wait(1)

c.click('A')
c.wait(1)

c.click('A')
c.wait(1)

c.click('A')
c.wait(1)

c.wait(45)

c.click('Y')
c.wait(30)

c.disconnect('Sample')