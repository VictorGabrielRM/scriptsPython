from pysimplesoap.client import SoapClient


location = "http://10.2.19.18/otrs/nph-genericinterface.pl/Webservice/name_webservice"
namespace = "namespace"
operation = "operation"

ticket_type = "INCIDENTE"
ticket_title = "Criando chamado com python"

ticket_customer = 'otrs.normal'
ticket_queue = 6
ticket_service_id = 1
ticket_state = "open"
ticket_sla_id = ''

article_subject = ticket_title
article_body = "Criando chamado com python 3.5 com a lib pysimplesoap 1.6"
article_content_type = "text/plain; charset=iso-8859-1"

ticket = {'Type': ticket_type,
		  'Title': ticket_title,
		  'CustomerUser': ticket_customer,
		  'QueueID': ticket_queue,
		  'ServiceID': ticket_service_id,
		  'State': ticket_state,
		  'SLAID': ticket_sla_id,
		  'PriorityID': '1'}

article = {'Subject': article_subject, 
		   'Body': article_body, 
		   'ContentType': article_content_type}

client = SoapClient(location = location,
					action = namespace + '#' + operation,
					namespace = namespace
					)

result = client.CriarChamadoGSC(Ticket=ticket,Article=article, Password='stefanini', UserLogin='otrs.stefanini')