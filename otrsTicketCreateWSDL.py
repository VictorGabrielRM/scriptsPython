from suds.client import Client


url = 'http://localhost/otrs-web/TicketConnector.wsdl'

client = Client(url)


ticketCreate = client.factory.create('OTRS_TicketCreate')

ticketCreate.Ticket['Title'] = "TESTE "
ticketCreate.Ticket['CustomerUser'] = "otrs"
ticketCreate.Ticket['QueueID'] = 6
ticketCreate.Ticket['Type'] = 'INCIDENTE'
ticketCreate.Ticket['ServiceID'] = ''
ticketCreate.Ticket['StateID'] = 1
ticketCreate.Ticket['SLAID'] = ''
ticketCreate.Ticket['PriorityID'] = 1

ticketCreate.Article['Subject'] = "TESTE ! FAVOR NÃO INTERAGIR!!"
ticketCreate.Article['Body'] = "TESTE ! FAVOR NÃO INTERAGIR!!"
ticketCreate.Article['ContentType'] = "text/plain; charset=iso-8859-1"


ticketCreate.DynamicField = [{'Name': 'externalNumber', 'Value': '300-000'}]


ticketCreate.DynamicField.append({'Name': 'Teste', 'Value': '010203'})
ticketCreate.DynamicField.append({'Name': 'emailTeste', 'Value': 'email@email.com'})
ticketCreate.DynamicField.append({'Name': 'enderecoTeste', 'Value': 'endereço de teste'})
ticketCreate.DynamicField.append({'Name': 'idTeste', 'Value': '000'})
result = client.service.TicketCreate(ticketCreate)

ticketCreate.Password = 'password'
ticketCreate.UserLogin = 'login'
result = client.service.TicketCreate(ticketCreate)

