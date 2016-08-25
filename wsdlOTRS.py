from suds.client import Client


url = 'http://localhost/otrs-web/TicketConnector.wsdl'

client = Client(url)

ticketGet = client.factory.create('OTRS_TicketGet')

ticketGet.Password = 'password'
ticketGet.TicketID = 9520
ticketGet.UserLogin = 'login'
ticketGet.ArticleOrder = 'DESC'
ticketGet.ArticleLimit = 1
ticketGet.AllArticles = 1

result = client.service.TicketGet(ticketGet)
