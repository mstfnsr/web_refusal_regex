refusal_regex_set = []

refusal_regex_set.append({
    "full_msg"  :   " cloudflare               please enable cookies.   sorry, you have been blocked you are unable to access artbattle.com            why have i been blocked? this website is using a security service to protect itself from online attacks. the action you just performed triggered the security solution. there are several actions that could trigger this block including submitting a certain word or phrase, a sql command or malformed data.   what can i do to resolve this? you can email the site owner to let them know you were blocked. please include what you were doing when this page came up and the cloudflare ray id found at the bottom of this page.      cloudflare ray id: 830aa4ef09258f0a •        your ip:       click to reveal 3.238.180.174 •  performance & security by cloudflare",
    #               "attention required! | cloudflare               please enable cookies.   sorry, you have been blocked you are unable to access givesmart.com            why have i been blocked? this website is using a security service to protect itself from online attacks. the action you just performed triggered the security solution. there are several actions that could trigger this block including submitting a certain word or phrase, a sql command or malformed data.   what can i do to resolve this? you can email the site owner to let them know you were blocked. please include what you were doing when this page came up and the cloudflare ray id found at the bottom of this page.      cloudflare ray id: 82f4e001c91f3aff •        your ip:       click to reveal 35.175.107.142 •  performance & security by cloudflare"
    #               "stackpath      access denied  partsplus.com.sv is using a security service for protection against online attacks. an action has triggered the service and blocked your request.   please try again in a few minutes. if the issue persist, please contact the site owner for further assistance.     reference id ip address date and time     dd931eb9522542e42ab2918fdf10f146 18.205.26.39 12/10/2023 08:01 pm utc      protected by stackpath"
    #               "cellartracker          stackpath  sorry, you have been blocked.            cellartracker is using a security service to protect itself from online attacks. you performed an action that triggered the service and blocked your request. if you believe this is a mistake, please email support@cellartracker.com and include the reference id below so we can further assist you.               reference id: 16e6a36c9440c40177fe192c8ca315d0                 security services provided by stackpath"
    "regex"     :   "^.{20,250}us(ing|es) a security service (to|for) protect(ion)? (itself from|against) online attacks",
    "type"      :   "block",
    "who"       :   "you",
    "why"       :   "security/malicious",
	"tag"		:	"cloudflare"
})

refusal_regex_set.append({
    "full_msg"  :   " cloudflare                      kokie-fayllarni yoqing.   kechirasiz, siz bloklangansiz sizga kira olmaysiz mypurewin.com             nega men bloklandim? ushbu veb-sayt o'zini onlayn hujumlardan himoya qilish uchun xavfsizlik xizmatidan foydalanmoqda. siz amalga oshirgan amal xavfsizlik yechimini ishga tushirdi. bu blokirovkaga sabab boʻlishi mumkin boʻlgan bir qancha harakatlar, jumladan, maʼlum bir soʻz yoki ibora, sql buyrugʻi yoki notoʻgʻri shakllangan maʼlumotlarni yuborish.   buni hal qilish uchun nima qilishim mumkin? siz elektron pochta orqali yuborishingiz mumkin. bloklanganligingizni bildirish uchun sayt egasi. iltimos, ushbu sahifa ochilganda nima qilayotganingizni va ushbu sahifaning pastki qismida joylashgan cloudflare ray id raqamini kiriting.      cloudflare ray id:8307a7969fe5372f  •        sizning ip:ochish uchun bosing 2a01:4f8:10b:183::2 •  manshoflik va xavfsizlik cloudflare",
    "regex"     :   "^\s{0,5}cloudflare\s{1,40}kokie-fayllarni yoqing.+bu veb-sayt o'zini onlayn hujumlardan himoya qilish uchun xavfsizlik xizmatidan foydalanmoqda\. siz amalga oshirgan amal xavfsizlik yechimini ishga tushirdi",
    "type"      :   "block",
    "who"       :   "you",
    "why"       :   "security/malicious",
	"tag"		:	"cloudflare"
})

refusal_regex_set.append({
    "full_msg"  :   "acesso bloqueado      acesso bloqueado não foi poss&iacutevel acessar rodolfooliveiracp.com.br     por que fui bloqueado? o site é protegido por um serviço de segurança online que o protege contra ataques. este acesso foi filtrado e classificado como indevido.   o que eu devo fazer? entre em contato por email com o dono do site, informando sobre o bloqueio. envie o id da requisição exibido abaixo para facilitar a investigação.      id da requisição: 13ed710bb95289e3a95f1ec11d40718b - seu endereço ip: 35.172.165.64 horário: 2023-12-11 05:13:43 - local: 1m1",
    "regex"     :   "^.{1,150}o site é protegido por um serviço de segurança online que o protege contra ataques",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	""
})

refusal_regex_set.append({
    "full_msg"  :   "not acceptable       406 - not acceptable request was blocked due to suspicious behavior  request details   time saturday, 09-dec-2023 17:11:15 gmt   ip 44.212.96.86   id zxsfsy7nymg0rhxh9qi25aaaapi",
    "regex"     :   "^not acceptable.{1,50}request was blocked due to suspicious behavior",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "403 - we detected that your latest request may have been part of suspicious activity and has been blocked. if you believe you are getting this message in error please let us know through our site&#039;s contact form.        403 - we detected that your latest request may have been part of suspicious activity and has been blocked. if you believe you are getting this message in error please let us know through our site's contact form.  you may not be able to visit this page because of:  an out-of-date bookmark/favourite a search engine that has an out-of-date listing for this site a mistyped address you have no access to this page the requested resource was not found. an error has occurred while processing your request.  please try one of the following pages:  home page  if difficulties persist, please contact the website administrator and report the error below.                   we detected that your latest request may have been part of suspicious activity and has been blocked. if you believe you are getting this message in error please let us know through our site's contact form.",
    "regex"     :   "^403.{1,20}we detected thatwe detected that your latest request may have been part of suspicious activity and has been blocked",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   " bsh hausgeräte gmbh    b/s/h   possible security risk detected    dear user, your request has been rated as suspicious by our firewall and therefore got blocked. if this is incorrect please get in touch with us via mcw-website-support@bshg.com by referring to   6761558716814731546.     © bsh hausgeräte gmbh. a company of the bosch group  data protection information imprint",
    "regex"     :   "^.{50,100}your request has been rated as suspicious by our firewall and therefore got blocked",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
    "full_msg"  :   "access denied | blog.elabogado.com uses sysadminok waf to restrict malicious requestsyou have been blockedhttps://blog.elabogado.com/2019/05/22/que-es-el-machine-learning/why have i been blocked?this website is using a security service to protect itself from online attacks, your access has been blocked for security reasons.how can i resolve it?you can email the website owner explaining what happened and include the information that appears below.your ip: 35.175.107.142date & time: 09/dec/2023:06:49:05 +0100request id: 646ed045f199e11376ae9259632e2e69performance & security by sysadminok",
    "regex"     :   "^access denied.{1,50}uses sysadminok waf to restrict malicious requests\s*you have been blocked",
    "type"      :   "block",
    "who"       :   "you",
    "why"       :   "security/malicious",
	"tag"		:	"sysadminok"
})    

refusal_regex_set.append({
    "full_msg"  :   "403 forbidden      a potentially unsafe operation has been detected in your request to this site your access to this service has been limited. (http response code 403) if you think you have been blocked in error, contact the owner of this site for assistance. block technical data   block reason: a potentially unsafe operation has been detected in your request to this site   time: thu, 30 nov 2023 3:57:18 gmt         about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation generated by wordfence at thu, 30 nov 2023 3:57:18 gmt.your computer's time: .",
    "regex"     :   "^403 forbidden\s{1,20}a potentially unsafe operation has been detected in your request to this site your access to this service has been limited",
    "type"      :   "block",
    "who"       :   "you",
    "why"       :   "security/malicious",
	"tag"		:	"wordfence"
})   

refusal_regex_set.append({
    "full_msg"  :   "block pageblockedsorry, your request is a suscipious threat to the website and blocked by the defense system.please contact the system administrator to whitelist your access if it is a false positive.your request id is ac11000117014103474186744ebc10",
    "regex"     :   "^block pageblockedsorry, your request is a suscipious threat to the website and blocked",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	""
})

refusal_regex_set.append({
    "full_msg"  :   "you have been blocked for suspicious spam!if you think there is an error, please contact us",
    "regex"     :   "^you have been blocked for suspicious spam",
    "type"      :   "block",
    "who"       :   "you",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
    "full_msg"  :   "you have been blocked for 72 hours due to three (3) incorrect userid/password entries, or other suspicious activities.   your ip address is: 34.229.63.28",
    "regex"     :   "^you have been blocked for \d+ hours due to .+ or other suspicious activities",
    "type"      :   "block",
    "who"       :   "you",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
    "full_msg"  :   "problem                                                       invalid request! the request to access this page was found to contain a potentially harmful request and has been blocked. if             you think that this is an error, please make our support team aware letting us know the link you attempted             to visit. return to site homepage",
    "regex"     :   "^problem.{1,100}invalid request! the request to access this page was found to contain a potentially harmful request and has been blocked",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	""
})

refusal_regex_set.append({
    "full_msg"  :   "aapanel website firewall free edition     aapanel website firewall free edition  your request has an illegal parameter and has been blocked by the webmaster settings! possible reason:   your submission contains dangerous attack requests  how to solve:   check the submission; if the website is hosted, please contact the space provider; for ordinary website visitors, please contact the webmaster; this is a false positive, please contact the aapanel https://forum.aapanel.com/",
    "regex"     :   "^aapanel website firewall.{10,100}your request has an illegal parameter and has been blocked",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	"aapenal"
})
refusal_regex_set.append({
    "full_msg"  :   "access restricted | shieldpro                \t\t\t\t\t\t\t\t\t\t\taccess restricted \t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t\taccess from your ip address has been temporarily restricted. \t\t\t\t\t\t\t\t\t     restriction details  \t\t\t\t\t\t    too many requests from your ip address have triggered the site's automated defenses. \t\t\t\t\t      \t\t\t\t\t\t    this website uses a security service to monitor requests to check for activity that is malicious, abnormal or unexpected. \t\t\t\t\t           restrictions lifted 6 days from now   your ip address 44.212.94.18   time now 10:15 pm december 7, 2023   homepage https://formerteenstars.com            \t\t      please contact site admin to request your ip address is unblocked. \t\t\t    \t\t\t      if you're the website administrator, \t\t\t      please review this guide. \t\t\t\t           about shield security for wordpress  \t\t\t\t\t        shield security is a powerful wordpress security service deployed on over 60,000+ wordpress websites. \t\t\t\t          \t\t\t\t\t        as a smarter approach to security, it quickly identifies & blocks malicious bots. \t\t\t\t\t        it prevents spam on comments and contact forms, blocks brute-force logins, rate-limits abusive traffic, \t\t\t\t\t        and scans for malware and similar file hacks. \t\t\t\t         more information can be found at https://getshieldsecurity.com            unblock your ip                 unblock your ip",
    "regex"     :   "^access restricted \| shieldpro.+too many requests from your ip address have triggered",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "excessive/suspicious",
	"tag"		:	"shieldpro"
})
refusal_regex_set.append({
    "full_msg"  :   "405                   sorry, your request has been blocked as it may cause potential threats to the server's security.           your request id is :  2ff6169717022472357441962e",
    "regex"     :   "^405\s{1,50}sorry, your request has been blocked as it may cause potential threats to the server's security",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "wp_die blocked your ip address has been blocked due to detected spam/malicious activity.  403",
    "regex"     :   "^wp_die blocked your ip address has been blocked due to detected spam/malicious activity",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "403403 forbiddenwhat does that mean?your request has been refused by the server.link11 is the specialized it security provider of protecting web services and infrastructures against cyber-attacks. this request is unable to complete due to the above error and has not been filtered by link11.id: 1390506592, your ip address: 18.205.26.39timestamp: sun, 10 dec 2023 14:12:28 gmt",
    "regex"     :   "^403.{10,50}your request has been refused by the server.{1,100}is the specialized it security provider of protecting web services and infrastructures against cyber-attacks",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	"link11"
})
refusal_regex_set.append({
    "full_msg"  :   "oops..      🤭 oh! this page is protected against cyber attacks and your ip has been banned by our system. checked your network for suspicious activity! this security check has been powered by                    crowdsec",
    "regex"     :   "^oops\.\..{1,30}this page is protected against cyber attacks and your ip has been banned by our system",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "security/malicious",
	"tag"		:	"crowdsec"
})
refusal_regex_set.append({
    "full_msg"  :   "u bent geblokkeerd wegens mogelijk misbruik you have been blocked for possible abuse  mogelijk gebruikt u, om adressen via onze gratis zoekmachine te zoeken, een datacenter of ip waar vele gebruikers op zitten. één of meerdere van deze gebruikers maakt misbruik van onze site. onder misbruik valt het automatisch verkrijgen van postcodegegevens van onze websites door middel van een online koppeling met het zoekformulier, of op een andere wijze.  hierdoor zijn wij genoodzaakt een blokkade in stellen voor het gehele datacenter waardoor deze melding wordt getoond. het is helaas niet mogelijk om deze blokkade op te heffen.  voor het automatiseren van dergelijke opvragingen en het integreren van zoekfunctionaliteiten biedt postcode.nl diverse betaalde productoplossingen, welke niet worden geblokkeerd.  voor integratie o.a. in een webshop, crm/erp systeem, saas platform: postcode.nl adres api voor integratie in een database systeem: nationale postcodedatabase  (c) postcode.nl b.v.  julianastraat 30 2012 es haarlem tel. 023 532 56 89 fax 023 531 43 32 [email protected]  onze adres producten  voor een api integratie: postcode.nl adres api voor een database systeem: nationale postcodedatabase",
    #translation:   you have been blocked for possible abuse. To search for addresses via our free search engine, you may be using a data center or IP that has many users. one or more of these users abuses our site. Abuse includes automatically obtaining zip code data from our websites through an online link with the search form, or in another way. As a result, we are forced to set a block for the entire data center, which causes this message to be displayed. Unfortunately it is not possible to remove this blockage. postcode.nl offers various paid product solutions for automating such requests and integrating search functionalities, which are not blocked. for integration into a webshop, CRM/ERP system, SaaS platform: postcode.nl address API for integration into a database system: national postcode database (c) postcode.nl b.v. julianastraat 30 2012 es haarlem tel. 023 532 56 89 fax 023 531 43 32 [email protected] our address products for an API integration: postcode.nl address API for a database system: national postal code database
    "regex"     :   "^u bent geblokkeerd wegens mogelijk misbruik you have been blocked for possible abuse",
    "type"      :   "block",
    "who"       :   "you",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "suspicious activity detected, your ip address 3.80.4.147 has been blocked.blocking reason: path is /amafoundation/wp-content/uploads/sites/35/2020/10/my-story-ptmm.pdfthis is not a real blocking - the test mode of the \"antiscan\" module is on!",
    "regex"     :   "^suspicious activity detected, your ip address \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} has been blocked",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "dispersetech llc is secured by security pro           dispersetech llcis secured by security pro    we detected unusual activity from your ip 18.206.48.243 and has blocked access to this website. please confirm that you are not a robot.",
    "regex"     :   "^.{1,50} is secured by.{50,100}we detected unusual activity from your ip \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} and has blocked access to this website",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "excessive/suspicious",
	"tag"		:	"security pro"
})
refusal_regex_set.append({
    "full_msg"  :   "400 - forbidden    # modsecurity - bloquejat per seguretat / bloqueado por seguridad / blocked for security reasons el sistema de seguretat ha detectat que la seva petició és potencialment maliciosa. si us plau, posi's en contacte amb els administradors de la web. el sistema de seguridad ha detectado que su petición es potencialmente maliciosa. por favor, póngase en contacto con los administradores de la web. the server's security system has flagged your request as potentially malicious. please contact the website operators.  unique id: zwve8n01c41keeag0cndvqaaabe request time: saturday, 02-dec-2023 23:59:44 utc pangea.org - hosting solidari",
    "regex"     :   "^400.{1,10}forbidden\s{1,10}# modsecurity.{1,500}the server's security system has flagged your request as potentially malicious",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	"modsecurity"
})
refusal_regex_set.append({
    "full_msg"  :   "access blocked   \t\tваш запрос заблокирован  \tподсистема безопасности сайта обнаружила и заблокировала активность, которая потенциально может быть небезопасной. \tпопробуйте использовать другой браузер, другой компьютер или выполнить запрос позже. \treason or support id: 8418e37e-fcae-4eda-8a58-c79d91e1a74b.",
    #translation:   access blocked \t\tyour request is blocked \tthe site's security subsystem has detected and blocked activity that could potentially be unsafe. \tTry using a different browser, another computer, or retry the request later. \treason or support id: 8418e37e-fcae-4eda-8a58-c79d91e1a74b.
    "regex"     :   "^access blocked.{10,50}подсистема безопасности сайта обнаружила и заблокировала активность, которая потенциально может быть небезопасной",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "security block          sorry, your request was blocked. we've recently detected malicious activity from your connection or network.    reqid: 25682958638987199 • ip: 35.175.107.142   security by cachewall",
    "regex"     :   "^security block\s{1,30}sorry, your request was blocked\. we.ve recently detected malicious activity from your connection or network",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "security/malicious",
	"tag"		:	"cachewall"
})
refusal_regex_set.append({
	"full_msg"  :   "error 406 - not acceptableerror 406 - not acceptablegenerally a 406 error is caused because a request has been blocked by mod security. if you believe that your request has been blocked by mistake please contact the web site owner.",
    "regex"     :   "^error 406.{40,100}because a request has been blocked by mod security",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "security/malicious",
	"tag"		:	"modsecurity"
})
refusal_regex_set.append({
	"full_msg"  :   "web application firewallweb application firewallthe transfer has triggered a web application firewall.       this transfer is blocked.      url: http://bibliotecas.upse.edu.ec/cgi-bin/koha/opac-search.pl?q=ccl=an:%2220929%22%20and%20su-to:cirugia&sort_by=relevance_dsc&limit=location:1 event id :  50130001      event type:  signature",
    "regex"     :   "^web application firewall.{0,50}web application firewall.{0,50}the transfer has triggered a web application firewall",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "security block     security block! requestor ip:  44.212.96.86  error ray id:  82fc152bbb525a33   we're sorry for the inconvenience but something about your request was flagged by our security system. if this is a persistent problem, please check out our faq for solutions to common issues at the mindbody security faq.  if you still can't resolve, please email securityblock@mindbodyonline.com at mindbody and include the ip address and ray id above.  we'll help you troubleshoot the issue as soon as we are able.  thank you. - mindbody security operations note:  please avoid emailing screenshots of this error page.  for accurate and efficient help, simply select and copy the ip and ray id text.",
    "regex"     :   "^security block",
    "type"      :   "block",
	"who"       :   "request",
	"why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "bot protection firewall blocked because of malicious activities reference id: 179549805965679d99ddff6",
    "regex"     :   "^bot protection.+firewall blocked because of malicious activities",
    "type"      :   "block",
    "who"       :   "",
    "why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "citeab - data accelerating science               suspicious activity detected suspicious activity from your network has been detected by one of our administrators. this may include detection of an attempt to scrape citeab.com, or another breach of our terms & conditions of use. your details have been referred to one of our team who will review usage of this website from your ip and network address. most of the time, there is nothing to worry about and we hope to have you unblocked shortly. however, if you are found to be in breach of the terms and conditions of this website, we reserve the right to take further action. if you feel you are seeing this message in error, please contact hello@citeab.com and we’ll do what we can to help. please include your ip address, which is 18.207.160.97   copyright © citeab . all rights reserved.",
    "regex"     :   "^.{1,80}suspicious activity detected suspicious activity from your network has been detected by one of our administrators",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "blocked    your ip address has been blocked due to detected spam/malicious activity.",
    "regex"     :   "^blocked\s{1,10}your ip address has been blocked due to detected spam/malicious activity",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "access forbidden       onlinetestcentre.com we detected suspicious activity from your ip (44.220.249.141) address or you are creating too big load to our web servers and therefore all requests from you are blocked. \t \tplease use form below to explain what happened and we will consider un-blocking. \t  email:  description of what happened:  send",
    "regex"     :   "^access forbidden\s{5,50}we detected suspicious activity from your ip \(.+\) address or you are creating too big load to our web servers and therefore all requests from you are blocked",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "your request has been blocked due to suspicious activity. if you feel this is in error please email support@ataira.com",
    "regex"     :   "^your request has been blocked due to suspicious activity",
    "type"      :   "block",
    "who"       :   "request",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
    "full_msg"  :   "your ip address: 3.233.221.90 was blocked because of suspicious activity.",
    "regex"     :   "^your ip address: \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} was blocked because of suspicious activity",
    "type"      :   "block",
    "who"       :   "ip",
    "why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "429 too fast, you are temporarily banned          banned status code: 429 too fast, you are temporarily banned   sprache | language | język:   de   en   pl      unser automatisches system hat ungewöhnlichen datenverkehr von deinem computer, aus deinem netzwerk oder von deinem internetanbieter festgestellt. um unser service für alle nutzer aufrecht erhalten zu können, wurdest du vorübergehend gesperrt.  die häufigsten gründe für eine sperre:   du verwendest eine vpn-verbindung da sich in letzter zeit missbräuchliche zugriffe aus vpn-netzen mehren, werden diese teilweise blockiert. deaktiviere daher bitte deine vpn-verbindung für die nutzung von geizhals oder füge in deinem vpn-client für folgende seiten/ip-adressen ausnahmen hinzu: geizhals.at (213.229.61.37), geizhals.de (213.229.61.34) oder geizhals.eu (81.223.238.139)   von deiner ip-adresse erfolgten verdächtigte zugriffe ein weiterer grund könnte sein, dass die von dir verwendete ip-adresse auf einer öffentlichen blacklist steht. du kannst dies hier (cleantalk.org) oder hier (abuseipdb.com) überprüfen.   du greifst mithilfe von scripts bzw. automatisiert auf unseren preisvergleich zu wir bitten dich, ein automatisiertes auslesen unseres preisvergleichs zu vermeiden.  um über preisänderungen informiert zu werden, kannst du unsere preisalarme verwenden um über neue produkte informiert zu werden, kannst du kategoriesuchen abonnieren um einen überblick über mehrere produkte zu behalten, kannst du wunschlisten anlegen      sperre aufheben       erfolgte deine sperre unberechtigt?  kein system ist perfekt, manchmal passieren leider fehler. bitte schicke uns eine e-mail an webmaster@geizhals.at und gib uns folgende ban-id bekannt: okjwmts7nuoalj==     our automated system has detected unusual traffic from your computer, your network or your isp. to ensure our service for all users we have temporarily blocked you.  most common reasons for a ban:   you are using a vpn connection vpn users are being blocked sometimes since there has been an increasing number of suspicious activities of vpn networks. please deactivate your vpn connection to continue using skinflint or add an exception to your vpn client for the following sites/ip-adresses: geizhals.at (213.229.61.37), geizhals.de (213.229.61.34) or geizhals.eu (81.223.238.139)   suspicious traffic from your ip address another reason could be that the ip address you are using is on a public blacklist. you can check this here (cleantalk.org) or here (abuseipdb.com).   you are accessing our website using scripts or automatized we are asking you to avoid an automated parsing of our website.  you can subscribe to our price alerts to be informed about price changes you can subscribe to the category searches to be informed about new products you can create wish lists to have an overview of multiple products      unban       was your ban unjustified?  no system works perfectly, sometimes mistakes can occur. please send us an email to webmaster@geizhals.at and share the following ban id with us: okjwmts7nuoalj==     nasz automatyczny system zauważył niezwyczajny transfer przez twój computer, twóją sieć albo twojego usługodawce internetu. aby nasz serwis dalej działał zablokowaliśmy cię tymczasowo.  najczęstsze powody na blok:   używasz połączenia vpn  sieci vpn mają często doczynienia z podejrzanymi połąceniami, dlatego są one przez nas blokowane. proszę zdeaktywuj twoje połączenie vpn albo dodaj te strony/adresy ip do wyjątków twojego clientu vpn: geizhals.at (213.229.61.37), geizhals.de (213.229.61.34) or geizhals.eu (81.223.238.139)    twój adres ip jest znany za podejrzane połącenia jeden powód może być, że twój adres ip jest na oficjalnej liście czarnej. sprawdź tutaj (cleantalk.org) albo tu (abuseipdb.com).   używasz naszą stronę automatycznie albo używasz skiptów  prosimy cię nie używać automatycznego wyczytywania naszej strony.   aby dostać informacje o zmianach cen możesz się zapisać na alarmy cenowe aby być poinformowany o nowych produktach możesz się zapisać na wyszukiwanie kategorii aby dostać lepszą orientacje o produkach możesz sobie ułożyć listy życzeń listy życzeń      odblokuj       zostałeś zablokowany bez powodu?  żaden system jest perfekcyjny, czasami zdarza się błąd. prosimy wysłac e-mail na adres webmaster@geizhals.at i podzielić sie ban-id: okjwmts7nuoalj==",
	"regex"     :   "^429.{1,10}too fast", 
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "access denied | albertagetrich.typepad.com used cloudflare to restrict access            please enable cookies.    error 1015  ray id: 82f054f46afd9c3d • 2023-12-02 03:02:34 utc you are being rate limited    what happened? the owner of this website (albertagetrich.typepad.com) has banned you temporarily from accessing this website.             was this page helpful?         yes no           thank you for your feedback!         cloudflare ray id: 82f054f46afd9c3d •        your ip:       click to reveal 3.239.2.192 •  performance & security by cloudflare",
	"regex"     :   "^access denied \| .{5,100}used cloudflare to restrict access.{80,150}you are being rate limited",	
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	"cloudflare"
})

refusal_regex_set.append({
	"full_msg"  :   "ups! parece que algo no va bien...                    coches.net    ups! parece que algo no va bien...     algo en tu navegador nos hizo pensar que eres un bot. hay algunas razones por las que esto podría suceder:  estás usando un complemento de navegador que está impidiendo que javascript se ejecute estás utilizando una vpn o un software de privacidad que usan con frecuencia los atacantes eres un usuario avanzado que se mueve a través de este sitio web con velocidad super humana         coches.net es parte de adevinta junto con fotocasa.eshabitaclia.cominfojobs.netmotos.netmilanuncios.comjobisjob © 2020 adevinta spain s.l.u.",
    #translation:   oops! It seems that something is not right... autos.net oops! It seems that something is wrong... something in your browser made us think that you are a bot. There are a few reasons why this could happen: You are using a browser plugin that is preventing Javascript from running You are using a VPN or privacy software that is frequently used by attackers You are a power user moving through this site website with super human speed cars.net is part of adevinta along with fotocasa.eshabitaclia.cominfojobs.netmotos.netmilanuncios.comjobisjob © 2020 adevinta spain s.l.u.
	"regex"     :   "^ups! parece que algo no va bien.+eres un usuario avanzado que se mueve a través de este sitio web con velocidad super humana",	
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "error: too many attempts, you will be able to try again january 5, 2028.",
	"regex"     :   "^error: too many attempts, you will be able to try again",	
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "page temporarily unavailablethis page is temporarily unavailable because a device from your location is sending large amounts of web requests. visitors from other locations can still view the page.what can i do?if you're a visitor to this storeplease try again in a couple minutes by refreshing the page.if you're the owner of this storetry again in a couple minutes by refreshing the page. if you’re still experiencing the issue, please contact shopify support for more information.",
	"regex"     :   "^page temporarily unavailable.{1,50}because a device from your location is sending large amounts of web requests",	
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	"shopify"
})

refusal_regex_set.append({
	"full_msg"  :   "access blocked - vymaps.comip address: 3.235.60.197you are accessing vymaps.com too much.. if you think this is an error, please use this link to fix this error.",
	"regex"     :   "^access blocked.{1,50}ip address:.{10,50}you are accessing .{1,50} too much",	
    "type"      :   "block",
	"who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "windows   mac windows                your ip address (44.212.94.18) has been temporarily blocked because of the large amount of requests we have received from it over a short period of time.     please fill out the following form to have your request processed:      request completion form        about us  who we are terms & privacy news feedback & support    users  members forum faq    developers  advertising general information submit/update program dmca/request content removal    software  answers top software formac all downloads     copyright © 2023, informer technologies, inc.",
	"regex"     :   "^.{1,50}your ip address \(.+\) has been temporarily blocked because of the large amount of requests we have received from it over a short period of time",	
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "your access to this site has been limited      your access to this site has been limited by the site owner your access to this service has been limited. (http response code 503) if you think you have been blocked in error, contact the owner of this site for assistance.  if you are a wordpress user with administrative privileges on this site please enter your email in the box below and click \"send\". you will then receive an email that helps you regain access.        block technical data   block reason: exceeded the maximum number of requests per minute for crawlers.   time: thu, 30 nov 2023 20:29:52 gmt         about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation (opens in new tab) generated by wordfence at thu, 30 nov 2023 20:29:52 gmt.your computer's time: .    ",
    #               "(the same beginning)-> block technical data   block reason: exceeded the maximum global requests per minute for crawlers or humans.   time: thu, 7 dec 2023 21:16:56 gmt        about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation (opens in new tab) generated by wordfence at thu, 7 dec 2023 21:16:56 gmt.your computer's time: .           
    #               "(the same beginning)-> block technical data   block reason: превышено максимальное количество запросов в минуту для краулеров.   time: mon, 11 dec 2023 12:10:59 gmt         about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation generated by wordfence at mon, 11 dec 2023 12:10:59 gmt.your computer's time: .",
    #               "(the same beginning)-> block technical data\s*block reason:\s*arama motoru robotları veya insanlar için bir dakikada olabilecek en fazla genel istek sayısı aşıldı
    #               "(the same beginning)-> block technical data\s*block reason:\s*het maximale aantal aanvragen per minuut voor crawlers overschrede
    #               "(the same beginning)-> block technical data\s*block reason:\s*se superó el número máximo de solicitudes de páginas por minuto alcanzado por rastreadores
    #               "(the same beginning)-> block technical data\s*block reason:\s*クローラーまたは人間による1分あたりのグローバルリクエストの最大値を超えました
    #               "(the same beginning)-> block technical data\s*block reason:\s*przekroczono maksymalną liczbę błędów .nie znaleziono strony. na minutę dla robota indeksującego
    #               "(the same beginning)-> block technical data\s*block reason:\s*número máximo de solicitações de páginas por minuto para rastreadores excedido
    #               "(the same beginning)-> block technical data\s*block reason:\s*exceeded the maximum number of page requests per minute for humans
	"regex"     :   "^your access to this site has been limited.+block technical data\s*block reason:\s*(exceeded the)|(превышено максимальное)|(arama motoru robotları)|(het maximale)|(se superó el número máximo)|(クローラーまたは人間)|(przekroczono maksymalną liczbę)|(número máximo de)",	
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	"wordfence"
})

refusal_regex_set.append({
	"full_msg"  :   "blocked: security by cleantalk        security firewall is activated for your ip 18.205.26.39   blocked by traffic control maybe you've been blocked by a mistake. please refresh the page (press ctrl + f5) or try again later. the page was generated at sun, 10 dec 2023 16:40:46   1080599,  www.solonovelanegra.es   security by cleantalk   ",
	#               (same beginning)-> "security firewall is activated for your ip.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*blockiert durch verkehrssteuerung",	
    "regex"     :   "^blocked: security by.{1,50}security firewall is activated for your ip",	
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	"cleantalk"
})

refusal_regex_set.append({
	"full_msg"  :   "ddos protection message: you have been blocked for some minutes due to a high amount of aggressive requests. please use the api to gather large collections of data.",
	"regex"     :   "^ddos",
    "type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "ddos-guard",
    "regex"     :   "^ddos-guard$",
    "type"      :   "block",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "ddos protection | cleantalk        ddos protection is activated for your ip 3.80.4.147  please click bellow to pass protection,  or you will be automatically redirected to the requested page after 0 seconds.   to continue working with web-site, please make sure that you have enabled javascript.                         ddos protection by cleantalk  please enable javascript to see the requested page.",
    "regex"     :   "^ddos protection \| cleantalk",
    "type"      :   "checking",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	"cleantalk"
})

refusal_regex_set.append({
	"full_msg"  :   "forbidden if you are not a bot, please copy the report and send it to our support team. copy",
	"regex"     :   "^forbidden if you are not a bot, please copy the report",	
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "firewall blocked because of malicious activities reference id: 712601145656dd396b6e2f",
    #               "malcare firewall blocked because of malicious activities reference id: 16409617866573f9f5b2b4b",
	#               "jameson security firewall blocked because of malicious activities reference id: 166537856656fa659c27e9",
    #               "blogvault firewall blocked because of malicious activities reference id: 952130791656fb3c044cfe",
    #               "imark backup and protect firewall blocked because of malicious activities reference id: 189224281365762592cf7ad",
    #               "jijonline wordpress backup & security plugin firewall blocked because of malicious activities reference id: 106005686568cfe325285",
    #               "wordpress backup & security plugin - blogvault firewall blocked because of malicious activities reference id: 782156465767a384c5dd",
    #               "180 sites management software firewall blocked because of malicious activities reference id: 20721721836568f82c1c929",
    #               "sharpvault - backups & security firewall blocked because of malicious activities reference id: 21215798746568f17dde0a5",
    "regex"     :   "^.{0,100}firewall blocked because of malicious activities",	
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "security/malicious",
	"tag"		:	"blogvault/malcare"
})

refusal_regex_set.append({
	"full_msg"  :   "our security system is reporting unusual activity    our security system is reporting unusual activity. pre-cautionary/corrective action applied: block.  if you feel this is in error, please contact us at email \"info  @  the domain you are trying to reach\"",
    "regex"     :   "^our security system is reporting unusual activity.{60,100}action applied: block",
    "type"      :   "block",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "you might have been detected and blocked as a crawler bot! news corp australia uses software that manages crawler bot traffic on our websites. if you receive this message and are not a crawler bot (and are just a reader or subscriber), please try these steps first:  temporarily disable any adblockers / pop-up blockers / script blockers you have enabled add this site in to the allowed list for any adblockers / pop-up blockers / script blockers you have enabled ensure your browser supports javascript (this can be done via accessing https://www.whatismybrowser.com/detect/is-javascript-enabled in your browser) ensure you are using the latest version of your web browser   if you still need to be unlocked as a reader, subscriber or crawler bot, please e-mail us at accessissues@news.com.au and provide the ip address and reference number shown here along with why you require access.      your ip address is: 3.239.2.192 | your reference number is: 0.66c83017.1702095706.8ef80aa4     news corp australia.  ",
    "regex"     :   "^you might have been detected and blocked as a crawler bot",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "it appears that you are trying to extract information from this website using 'ccbot/2.0 (https://commoncrawl.org/faq/)'. the site will abort process now. thank you, have a nice day.",
    "regex"     :   "^it appears that you are trying to extract information from this website",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "blocked by wordpress zero spam    you have been blocked from visiting this site by wordpress zero spam due to detected spam activity.",
    #               "you have been blocked from visiting this site by wordpress zero spam due to detected spam activity."
    "regex"     :   "^(blocked by|you have been blocked).{30,150}due to detected spam activity",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	"zero spam"
})

refusal_regex_set.append({
	"full_msg"  :   "http 403         ️                          http 403                                 accès interdit                                                          cette requête a été bloquée par une sécurité activée sur l'hébergement.                si vous êtes le webmaster de ce site, vous pouvez désactiver cette sécurité depuis votre compte cpanel.                                                comment gérer cette sécurité avec tigerprotect dans cpanel ?                     nom de la règle de sécurité déclenchée  : badbots        [email protected]           -           tiger protect  request id : 3d33b7a495b23233765658a14f8e760e  ",
    "regex"     :   "^http 403.{20,300}cette requête a été bloquée par une sécurité activée sur l'hébergement",
	"type"      :   "block",
    "who"       :   "reqeust",
	"why"       :   "security/malicious",
	"tag"		:	"tiger protect"
})

refusal_regex_set.append({
	"full_msg"  :   "sorry...googlesorry...we're sorry...... but your computer or network may be sending automated queries. to protect our users, we can't process your request right now.see google help for more information.google home",
    "regex"     :   "^sorry\.\.\.googlesorry\.\.\.we're sorry\.{6} but your computer or network may be sending automated queries",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	"google"
})

refusal_regex_set.append({
	"full_msg"  :   "server too busy for web crawlers. please try again later.",
    "regex"     :   "^server too busy for web crawlers",
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "ip blocked    blocked spider access!",
    "regex"     :   "^ip blocked.{1,5}blocked spider access",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "403 access forbidden                            ✋                   we're sorry, you are not allowed to proceed your request looks suspiciously similar to automated requests from spam posting software or it has been denied by a security policy configured by the website administrator. if you believe you should be able to perform this request, please let us know.  rid: vq6lbh3ens7iiuo5jzvbwzaq                           know more: documentation|",
    #               "403 access forbidden                            ✋                   申し訳ありませんが、続行できません your request looks suspiciously similar to automated requests from spam posting software or it has been denied by a security policy configured by the website administrator. if you believe you should be able to perform this request, please let us know.  rid: sw2jx8t3t9akqblhmv4gcfyu"
    "regex"     :   "^403 access forbidden.{30,120}your request looks suspiciously similar to automated requests from spam posting software",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "we're sorry but your query looks similar to automated requests from a computer virus or spyware application. to protect our users, we can't process your request right now. if this is not the case, pls contact us (ref: 44.212.96.86, 2023-12-03 05:37:27) and someone will look at this as soon as possible",
    "regex"     :   "^we're sorry but your query looks similar to automated requests",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "automated request detected          ntldstats    automated request detected  dear user, your access to our website has been blocked automatically. this usually happens when we identify certain patterns that are similar to automated requests (crawling) with malicious intent. please note: access to ntldstats from vpns, cloud providers or dedicated/shared hosting ip ranges (like rackspace, ovh, amazon, google cloud, azure, alibaba, etc.) is being blocked in general. please use mobile internet or a common dsl/cable connection to access our website. thanks!if this is the first time this happens to you, please copy the information below and send it to mail@ntldstats.com - we will then review your request and get back to you. if your access has already been unlocked in the past, further reactivations of access will induce a reactivation fee. please send us the following information: remote ip:  35.175.107.142 user agent: ccbot/2.0 (https://commoncrawl.org/faq/) referer:    (none) protocol:   http/1.1 method:     get host:       ntldstats.com requested:  monday, 11-dec-2023 15:07:11 gmt  should we receive more requests of the same nature from your host(s) without hearing from you, your ip range will be blacklisted and - should it be deemed necessary - reported to your isp, ripe and/or local authorities like law enforcement agencies or district attorneys offices.     copyright © 2017 greensec gmbh, all rights reserved.  faq | privacy policy | imprint|",
    "regex"     :   "^automated request detected",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "error 403    error 403 - forbidden you want to crawl www.pharmaforce.fr ? contact us: contact(at)apotekisto(dot)fr          ",
    "regex"     :   "^error 403.{10,50}you want to crawl",
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "access deniedaccess denied from your country us, united states of america we're sorry but the site cannot be accessed from your country. your ip address 18.206.12.157 is not allowed to access our website. we have blocked access to the website due to one of two reasons:  we do not provide services in the country from which you are accessing our website. our system has detected unauthorized practices putting a strain on our website,  such as scanning, web scraping, ddos attacks, and monitoring the site without our consent.  if you are our customer and believe that the blockage is a mistake,  please urgently contact our customer support department.  in the case where the blockage was imposed for a reason other than  blocking access due to regional reasons, the ip address block will be automatically removed  after 24 hours of inactivity from that address. you can remove the blockade right now by declaring that you are human and clicking the button. ",
    "regex"     :   "^access deniedaccess denied from your country us",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "geoblock",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "country blocked         bg_error_lines    circle_dots                 country blocked access to this page is forbidden.   clouds_shape",
    "regex"     :   "^country blocked",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "geoblock",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "forbidden - visitors from your country are not permitted to browse this site.",
    #               "we are sorry; visitors from your country are not permitted to browse this site."
    #               "en visitors from your country are not permitted to browse this site.  de es sind nur besucher aus deutschland erlaubt. falls sie diese meldung bekommen, nutzen sie einen proxy o.ä. um ihre herkunft zu verschleiern."
    #               "запрет на вашу страну. whatsapp для заказов +79150970797 forbidden - visitors from your country are not permitted to browse this site."
    #               "dear visitor; we are sorry - visitors from your country are not permitted to browse this site."
    "regex"     :   "^.{0,70}visitors from your country are not permitted to",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "geoblock",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "fazzoletto in f.r.p. per connettori fibrenet in confezione da 25 pz - steacom s.r.l.steacom503 overloadedyou cannot access this store from your country. we apologize for the inconvenience.",
    #               "juliette ramadejuliette ramade503 overloadedyou cannot access this store from your country. we apologize for the inconvenience
    "regex"     :   "^.{10,200}you cannot access this store from your country",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "geoblock",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "wordpress › fehler    your ip address is blocked.  reason: your location (us) has been blocked.  please contact an administrator.",
    "regex"     :   "^wordpress.{10,20}your ip address is blocked\.  reason: your location \(us\)",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "geoblock",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "error 403: access denied      connection denied by ip2location country blocker please contact web administrator for assistance.  ip geolocation powered by ip2location.com     ",
    "regex"     :   "^.{1,100}ip2location country blocker",
    "type"      :   "block",
	"who"       :   "ip",
	"why"       :   "geoblock",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "(available|provided|blocked|service(s)?|offer|visitor(s)?|because|store|access|gambling|users|prohibited|forbidden) (in|from|for|of|forbidden) your country",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "geoblock",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "blockedyour request has been blocked.if you have questions, please contact us",
    "regex"     :   "^blockedyour request has been blocked\.if you have questions, please contact us",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "your access to this site has been limited by the site owner      your access to this site has been limited by the site owner your access to this service has been limited. (http response code 503) if you think you have been blocked in error, contact the owner of this site for assistance.  if you are a wordpress user with administrative privileges on this site, please enter your email address in the box below and click \"send\". you will then receive an email that helps you regain access.        block technical data   block reason: advanced blocking in effect.   time: sun, 10 dec 2023 22:30:53 gmt         about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation generated by wordfence at sun, 10 dec 2023 22:30:53 gmt.your computer's time: .",
    #               "your access to this site has been limited by the site owner      your access to this site has been limited by the site owner your access to this service has been limited. (http response code 503) if you think you have been blocked in error, contact the owner of this site for assistance.  if you are a wordpress user with administrative privileges on this site, please enter your email address in the box below and click \"send\". you will then receive an email that helps you regain access.        block technical data   block reason: accessed a banned url   time: tue, 28 nov 2023 8:41:18 gmt         about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation generated by wordfence at tue, 28 nov 2023 8:41:18 gmt.your computer's time: .",
    #               "your access to this site has been limited by the site owner      your access to this site has been limited by the site owner your access to this service has been limited. (http response code 503) if you think you have been blocked in error, contact the owner of this site for assistance.  if you are a wordpress user with administrative privileges on this site, please enter your email address in the box below and click \"send\". you will then receive an email that helps you regain access.        block technical data   block reason: access from your area has been temporarily limited for security reasons.   time: wed, 6 dec 2023 6:52:35 gmt        about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation generated by wordfence at wed, 6 dec 2023 6:52:35 gmt.your computer's time: .    ",
    #               "|your access to this site has been limited      your access to this site has been limited by the site owner your access to this service has been limited. (http response code 503) if you think you have been blocked in error, contact the owner of this site for assistance.  if you are a wordpress user with administrative privileges on this site please enter your email in the box below and click "send". you will then receive an email that helps you regain access.        block technical data   block reason: advanced blocking in effect.   time: sat, 2 dec 2023 14:10:36 gmt         about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation (opens in new tab) generated by wordfence at sat, 2 dec 2023 14:10:36 gmt.your computer's time: ."
    "regex"     :   "^.{0,20}your access to this site has been limited",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	"wordfence"
})

refusal_regex_set.append({
	"full_msg"  :   "your ip address is blocked. if you this an error, please contact webmaster!",
    "regex"     :   "^your ip address is blocked\. if you this an error",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "not acceptable       406 - not acceptable request was blocked due to suspicious behavior  request details   time saturday, 02-dec-2023 01:47:55 gmt   ip 34.229.63.28   id zwqmy6wv4igwfgz6e6xg-qaaaca  ",
    "regex"     :   "^not acceptable.{10,50}request was blocked due to suspicious behavior",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "your ip address: 44.212.96.86 was blocked because of suspicious activity.",
    "regex"     :   "^your ip address: .{6,39} was blocked because of suspicious activity",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "this website is secured against online attacks. your request was blocked due to suspicious behavior   client ip : 3.235.60.197  incident time : 2023-11-29 12:54:18 utc    incident id : zwc0enf6zylt8l0ybajiuqaaaik  if you feel it was a legitimate request, please contact the website owner for further investigation and remediation with a screenshot of this page.  ",
    "regex"     :   "^this website is secured against online attacks\. your request was blocked due to suspicious behavior",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "your request has been blocked due to suspicious activity. if you feel this is in error please email support@ataira.com",
    "regex"     :   "^your request has been blocked due to suspicious activity",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "403 your ip address has been blocked due to suspicious behavior. if you feel this was in error, please contact the website administrator.                                     home       about          back     autismclassroom.com       autism             courses       books          back     books       workbooks       journals             blog       social skills          back     social interaction       communication      ",
    "regex"     :   "^403 your ip address has been blocked due to suspicious behavior",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "403 request blocked    request blocked your request has been blocked due to suspicious activity.      servername : waf-master-vm     localtime : december 1, 2023, 12:42 am transactionid : ae68fb9dcc7fdef65764c50dfa4ee1b8remote address : 18.207.160.97remote country : (us)        method : get requested url : https://www.edouard-faller.fr/nous-contacter      protocol : http/1.1    user agent : ccbot/2.0 (https://commoncrawl.org/faq/)                     please contact the webmaster of this website and provide the information above if you think this is a mistake.          return to  www.edouard-faller.fr",
    "regex"     :   "^403 request blocked.{1,5}request blocked your request has been blocked due to suspicious activity",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "your ip address 18.206.48.243 has been blocked due to malicious activity reported to https://www.abuseipdb.com",
    "regex"     :   "^your ip address .{6,39} has been blocked due to malicious activity reported to",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "access denied           this page has been blocked by our protection services  1. why your ip address has been blocked? this website uses online threat protection and attacks mitigation system. your last request was unfortunately blocked by our system due to malicious activity. there are several reasons why this may have happened and the website owner has been notified.   2. how do i regain access to gps-access.fr? you can try to visit this page again later or contact the website owner. normally the website will revert to normal operations after a period of time. if you need further information please contact our support team on [email protected].   security provided by virusdie © virusdie.com : powered by virusdie.",
    "regex"     :   "^access denied.{50,100}why your ip address has been blocked",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "security/malicious",
	"tag"		:	"virusdie"
})
refusal_regex_set.append({
	"full_msg"  :   "denied | stuff.co.nz    denied this request has been refused by stuff.co.nz due to undesirable or unauthorised activity. if you believe this is in error, please raise with the domain technical contact.",
    "regex"     :   "^denied \|.{40,100}due to undesirable or unauthorised activity",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "access restricted | shieldpro                \t\t\t\t\t\t\t\t\t\t\taccess restricted \t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t\taccess from your ip address has been temporarily restricted. \t\t\t\t\t\t\t\t\t     restriction details  \t\t\t\t\t\t    in collaboration with crowdsec and their crowd-sourced ip reputation data, your ip address has been identified as malicious. \t\t\t\t\t      \t\t\t\t\t\t    all access to this website is therefore restricted. please take a moment to review your options below. \t\t\t\t\t           restrictions lifted za 23 godziny   your ip address 44.212.94.18   time now 23:16 11 grudnia, 2023   homepage https://gamp.pl        unblock my ip       \t\t      please contact site admin to request your ip address is unblocked. \t\t\t    \t\t\t      if you're the website administrator, \t\t\t      please review this guide. \t\t\t\t           about shield security for wordpress  \t\t\t\t\t        shield security is a powerful wordpress security service deployed on over 60,000+ wordpress websites. \t\t\t\t          \t\t\t\t\t        as a smarter approach to security, it quickly identifies & blocks malicious bots. \t\t\t\t\t        it prevents spam on comments and contact forms, blocks brute-force logins, rate-limits abusive traffic, \t\t\t\t\t        and scans for malware and similar file hacks. \t\t\t\t         more information can be found at https://getshieldsecurity.com            unblock your ip         you can automatically unblock your ip address by clicking the button below.                   unblock my ip address                      ",
    "regex"     :   "^access restricted \| .{100,350}in collaboration with crowdsec and their crowd-sourced ip reputation data, your ip address has been identified as malicious",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	"shieldpro"
})


refusal_regex_set.append({
	"full_msg"  :   "555 security incident detected     555 security incident detected your request was blocked. if you are the owner of the website: the website application firewall that is protecting your website has blocked this request for being suspicious. you can see the detailed reason for this in your webserver logs. if you are the visitor: the public ip address assigned to you, by your internet provider, might be suffering from poor reputation: look up ip reputation here. ip addresses from vpn providers or public networks often have poor reputation.  35.175.107.142",
    "regex"     :   "^555 security incident detected.{250,350}the public ip address assigned to you, by your internet provider, might be suffering from poor reputation",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "request blockeddue to abuse from this hosting service, all traffic is blocked.if you are a person and not a robot, please disable your vpn/proxy server to continue.",
    "regex"     :   "^request blockeddue to abuse from this hosting service, all traffic is blocked",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "cidram        access denied!  access denied!    id: 1701881505-830238-2753890834 script version: cidram v3.4.2 date/time: wed, 06 dec 2023 16:51:45 +0000 ip address: 44.197.101.x user agent: ccbot/2.0 (https://commoncrawl.org/faq/) signatures count: 2 signatures reference: 44.192.0.0/10, botua.php:l215 why blocked: cloud service (\"amazon.com, inc\", l11750:f0, [us]), backlink/seo/scraper ua! reconstructed uri: https://spiritandsoap.com/product-tag/st-johns-wort/ hostname: -     generated by cidram v3.4.2",
    "regex"     :   "^cidram.{1,10}access denied.{250,350}why blocked: cloud service",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	"cidram"
})
refusal_regex_set.append({
	"full_msg"  :   "www.illustrationerz.ca is protected by blockscript. \t\t\t\tblockscript is security software which protects websites and empowers webmasters to stop unwanted traffic. \t\t\t\tyour request was blocked because you appear to be accessing this website from a hosting provider network, proxy server, or vpn server.     if you believe that you are seeing this message in error please click here to notify blocked.com.     ",
    "regex"     :   "^.{5,60}is protected by blockscript.{100,150}your request was blocked because you appear to be accessing this website from a hosting",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	"blockscript"
})
refusal_regex_set.append({
	"full_msg"  :   "anonymous proxy or vpn   anonymous proxy or vpn 403 forbidden make sure you are allowed to access this page. if you are using an anonymous proxy or vpn you'll need to disable it to access babysits. if this error persists, try opening your browser again.  refresh     babysits",
    "regex"     :   "^anonymous proxy or vpn.{60,100}if you are using an anonymous proxy or vpn",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "you have been blocked from this web site     you have triggered our security system monitor indications show that your ip address may have been used for malicious attacks. if you are here by accident or believe you should not be banned, please contact us using the details below  the finchley clinic web administrator  please note that this system is in place to protect you and us from malicious attacks, do not be offended if you are here by accident. the store owner has been notified please quote your ip number which is 35.175.107.142 your user agent was identified as:- ccbot/2.0 (https://commoncrawl.org/faq/) date:- 02/12/2023",
    "regex"     :   "^you have been blocked from this web site.{1,10}you have triggered our security system monitor indications show that your ip address may have been used for malicious attacks",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "attention!        sorry, this is not allowed. thank you for visiting our website, unfortunately our website protection system has detected an issue with your ip     address and wont let you proceed any further. if you feel this is an error, please submit a support request. thank you for your patience.  https://www.getastra.com/   go to homepage",
    "regex"     :   "^attention!.{50,100}unfortunately our website protection system has detected an issue with your ip",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "reputation",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "406 blocked406 blockeddie anfrage wurde durch die webserver firewall geblockt. sofern sie einen fehler vermuten, wenden sie sich bitte an den support.the request was blocked by the web server firewall. if you suspect an error, please contact support.",
    "regex"     :   "^406 blocked406 blockeddie anfrage wurde durch die webserver firewall geblockt",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "403 forbidden      a potentially unsafe operation has been detected in your request to this site your access to this service has been limited. (http response code 403) if you think you have been blocked in error, contact the owner of this site for assistance. block technical data   block reason: a potentially unsafe operation has been detected in your request to this site   time: sat, 2 dec 2023 1:14:05 gmt         about wordfence wordfence is a security plugin installed on over 4 million wordpress sites. the owner of this site is using wordfence to manage access to their site. you can also read the documentation to learn about wordfence's blocking tools, or visit wordfence.com to learn more about wordfence.   click here to learn more: documentation generated by wordfence at sat, 2 dec 2023 1:14:05 gmt.your computer's time: .",
    "regex"     :   "^403 forbidden.{1,20}a potentially unsafe operation has been detected in your request",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "security/malicious",
	"tag"		:	"wordfence"
})

refusal_regex_set.append({
	"full_msg"  :   "access denied | www.mammeoggi.it used cloudflare to restrict access            please enable cookies.    error 1006  ray id: 82f7fccf2b0f820e • 2023-12-03 01:20:30 utc access denied    what happened? the owner of this website (www.mammeoggi.it) has banned your ip address (44.197.101.251).             was this page helpful?         yes no           thank you for your feedback!         cloudflare ray id: 82f7fccf2b0f820e •        your ip:       click to reveal 44.197.101.251 •  performance & security by cloudflare  ",
    "regex"     :   "^access denied \| .{150,200}the owner of this website \(.+\) has banned your ip address",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	"cloudflare"
})
refusal_regex_set.append({
	"full_msg"  :   "jobbsys as         the administrator has blocked your ip from accessing this website.    \t\t\t\tpowered by\t\t\t\tdefender                                    ",
    "regex"     :   "^.{0,100}the administrator has blocked your ip from accessing this website",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	"defender"
})
refusal_regex_set.append({
	"full_msg"  :   "access denied      access denied                                        the ip address you are using has been blocked.",
    "regex"     :   "^access denied.{5,10}access denied.{5,50}the ip address you are using has been blocked",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "sorry, 172.18.130.2 has been banned.                               ",
    "regex"     :   "^.{0,50}sorry, (your address)?.{5,39} ha(s|ve) been b(anned|locked)",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "18.206.12.157 has been banned up to sat, 02 dec 2023 03:52:46 +0000",
    #               3.238.180.174 has been banned 
    "regex"     :   "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} has been b(anned|locked)",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "access forbidden：3.239.2.192   ",
    "regex"     :   "^access forbidden.{1,5}\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "sorry, you have been blocked. - you are unable to access the web page.          whoops!          you are unable to access the web page.",
    "regex"     :   "^sorry, you have been blocked",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "493         493  sorry, you have been blocked!  server: 外网 vm-usa_mic_prd-140 time: 2023-12-05t10:12:36+08:00 id: 1c93568dfea49f13d07b6a7dbc7d5687      v20221213, mic waf © 2022",
    "regex"     :   "^493.{5,20}sorry, you have been blocked",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "you have been banned from this site.if you think there has been a mistake, please contact the administrator via proxy server. ",
    "regex"     :   "^you have been banned from this site",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "hyannis country garden         you have been blocked from accessing this website.    \t\t\t\tpowered by\t\t\t\tdefender",
    "regex"     :   "^.{0,50}you have been blocked from accessing this website",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	"defender"
})
refusal_regex_set.append({
	"full_msg"  :   "403 forbiddensie wurden durch das sicherheitssystem der website blockiert.you have been blocked by the site's security system.ous avez été bloqué par le système de sécurité du site.вы заблокированы системой безопасности сайта.您已被該網站的安全系統阻止。ja, ich bin ein bot.yes, i am a bot.oui, je suis un botда, я бот.是的，我是一個機器人.nein, ich bin ein mensch.no i am a human being.non, je suis un humain.нет, я человек.不，我是一個人。",
    "regex"     :   "^403 forbidd.{40,100}you have been blocked by the site's security system",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "access denied | www.masmusculo.com uses sysadminok waf to restrict malicious requests you have been blockedhttps://www.masmusculo.com/blog/el-aislado-de-proteina-de-suero-multiproposito/why have i been blocked?this website is using a security service to protect itself from online attacks, your access has been blocked for security reasons.how can i resolve it?you can email the website owner explaining what happened and include the information that appears below.your ip: 44.220.249.141date & time: 28/nov/2023:13:01:39 +0100request id: c45c10b4f7660ae839ce008fdcf11614site owner email: [email protected]",
    "regex"     :   "^access denied \| .{5,50} uses .{5,40} to restrict malicious requests you have been blocked",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "security/malicious",
	"tag"		:	"sysadminok"
})
refusal_regex_set.append({
	"full_msg"  :   "you have been blocked.",
    "regex"     :   "^you have been blocked\.",
    "type"      :   "block",
	"who"       :   "you",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "security alert - parliamentarians for global action - mobilizing legislators as champions for human rights, democracy and a sustainable world.           security alert request dropped!  you have been banned! if you think this is wrong contact the site administrator. reference code: sec-defb-0001  home back    parliamentarians for global action - mobilizing legislators as champions for human rights, democracy and a sustainable world. © 2023 powered by elxis cms © 2006-2023",
    "regex"     :   "^security alert.{10,200}security alert request dropped",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "you have been blocked for suspicious spam!if you think there is an error, please contact us",
    "regex"     :   "^.you have been blocked for suspicious spam",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "oops..      🤭 oh! this page is protected against cyber attacks and your ip has been banned by our system. this security check has been powered by                        crowdsec",
    "regex"     :   "^.{0,10}oops.{10,50}is protected against cyber attacks and your ip has been banned",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "security/malicious",
	"tag"		:	"crowdsec"
})
refusal_regex_set.append({
	"full_msg"  :   "security risk information | bsh hausgeräte gmbh    b/s/h   possible security risk detected    dear user, your request has been rated as suspicious by our firewall and therefore got blocked. if this is incorrect please get in touch with us via mcw-website-support@bshg.com by referring to   6761558716821161082.     © bsh hausgeräte gmbh. a company of the bosch group  data protection information imprint ",
    "regex"     :   "^security risk information",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "ninjafirewall 403 forbiddensorry 44.197.101.251, your request cannot be processed.for security reasons, it was blocked and logged.if you believe this was an error please contact thewebmaster and enclose the following incident id:[ #6942904 ]",
    "regex"     :   "^ninjafirewall",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "security/malicious",
	"tag"		:	"ninjafirewall"
})
refusal_regex_set.append({
	"full_msg"  :   "you have been banned",
    "regex"     :   "^you ha(ve|s) been banned",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "access denied             access denied error code 1020   you do not have access to www.auburnschl.edu.the site owner may have set restrictions that prevent you from accessing the site.        error details     provide the site owner this information.  i got an error when visiting www.auburnschl.edu/education/school/school.php?sectiondetailid=76&linkid=nav-menu-container-1. error code: 1020 ray id: 82e47f27ddba0833 country: us data center: iad12 ip: 35.172.165.64 timestamp: 2023-11-30 16:34:14 utc  click to copy                 was this page helpful?         yes no           thank you for your feedback!                         performance & security by cloudflare",
    "regex"     :   "^.{0,200}(access denied|403).{30,120}the site owner may have set restrictions that prevent you from accessing the site",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	"cloudflare"
})
refusal_regex_set.append({
	"full_msg"  :   "acesso negado        o sistema de seguran&ccedila deste servidor bloqueou sua conexão. seu ip bloqueado é o: 35.175.107.142 o hostname deste servidor é o: sv1.k2host.com.br os motivos de seu bloqueio foram:  lfd: (mod_security) mod_security (id:430013) disparado pelo ip 35.175.107.142 (us/united states/ec2-35-175-107-142.compute-1.amazonaws.com): 1 in the last 3600 secs - fri dec  1 17:34:58 2023    por favor verifique o motivo do bloqueio acima e solucione-o, caso seja um bloqueio por falha de login e você desconheça o que o causou, verifique se não há algum dispositivo configurado com dados incorretos em sua rede ou se alguma outra pessoa usando a mesma conexão não provocou o bloqueio. caso contrário este bloqueio poderá voltar à ocorrer novamente. após isso você pode tentar desbloquear seu ip resolvendo o recaptcha:         desbloquear      caso não compreenda o motivo do bloqueio, ou precise de ajuda para solucioná-lo, por favor entre em contato com nossa equipe de suporte para maiores informações nota: nem todas as requisições de liberação serão efetuadas com sucesso a depender de como seu endereço ip foi bloqueado. se o desbloqueio falhar você precisará entrar em contato com nosso suporte para obter maiores informações.",
    "regex"     :   "^acesso negado.{5,10}o sistema de seguran&ccedila deste servidor bloqueou sua conexão. seu ip bloqueado é o",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	"modsecurity"
})
refusal_regex_set.append({
	"full_msg"  :   "403 forbidden : logged by e107.grupoalpinopinsapo.es        403 forbidden!       either the address you are accessing this site from has been banned for previous malicious behavior or the action you attempted is considered to be hostile to the proper functioning of this system. the detected reason(s) you were blocked are:vague, nutch like scraper (spd-0057). possibly hostile scraper/harvester (spd-0190). amazon web services. not an access provider isp. used by hackers, keyword spamming seo bots, and other unsavories (cld-0amz). checked for bypass -  your ip, domain name (if resolvable), the referring page (if any), query, post, user agent, time of access, and date have been logged and flagged for admin review. please either 1. stop the bad behavior, or 2. cease accessing this system.your connection details: record #: 1 time:  running: 0.4.10a3 / 75 host: ec2-44-220-249-141.compute-1.amazonaws.com ip: 44.220.249.141 post:  query:  stripped query:  referer:  user agent: ccbot/2.0 (https://commoncrawl.org/faq/) reconstructed url: http:// e107.grupoalpinopinsapo.es /news.php     generated by zb block 0.4.10a3 / 75",
    "regex"     :   "^403 forbidden.{50,100}either the address you are accessing this site from has been banned for previous malicious behavior or the action you attempted is considered to be hostile",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "security/malicious",
	"tag"		:	"zb block"
})
refusal_regex_set.append({
	"full_msg"  :   "styleact.co.jp - access to the website is blocked.       styleact.co.jp access to the website is blocked.   incident id2023-12-08t21:55:55z|0c13f852be|34.228.52.21|j1otrzpnpk your ip address34.228.52.21 server ipxxx.xxx.xxx.178 codejsc-403 descriptionaccess blocked by website owner. please contact support.",
    "regex"     :   "^.{5,150}access to the website is blocked.{40,100}incident id",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "you are a spammer, hacker or an otherwise bad person. if you are the administrator of this site and have blocked your own ip address on accident please visit https://www.motopaedie-verband.de/administrator/index.php?admintools_rescue=you@example.com where you@example.com is the email address of your (super user) account. this url will only send you an email if the ip address from which you are accessing it is being blocked by admin tools. if you are not blocked no email will be sent; you don't need an email with instructions to unblock your ip if your ip is not blocked.",
    "regex"     :   "^you are a spammer, hacker or an otherwise bad person",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "security/malicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "crowdsec ban              crowdsec access forbidden  you are unable to visit the website.    this security check has been powered by                       crowdsec",
    "regex"     :   "^crowdsec ban",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	"crowdsec"
})
refusal_regex_set.append({
	"full_msg"  :   "you are not allowed to access this website, please contact the website administrator",
    "regex"     :   "^you are not allowed to access this website, please contact",
	"type"      :   "block",
    "who"       :   "you",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "anti-crawler protection is checking your browser and ip 18.206.12.157 for spam bots to continue working with the web site, please make sure that you have enabled javascript.   you will be automatically redirected to the requested page after 3 seconds.don't close this page. please, wait for 3 seconds to pass to the page.        the page was generated at sat, 02 dec 2023 15:15:49 browser time     798100, 13617,  https://riverleafmodels.us, 5.167   antispam by cleantalk        ",
    "regex"     :   "^.{0,250}(verify|check)(ing)? your (connection|browser)",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"cleantalk"
})

refusal_regex_set.append({
	"full_msg"  :   "human verification          javascript is disabled         in order to continue, you need to verify that you're not a robot by solving a captcha puzzle.          the captcha puzzle requires javascript. enable javascript and then reload the page.",
    "regex"     :   "^human verification\s{1,50}javascript is disabled",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"cloudfront"
})

refusal_regex_set.append({
	"full_msg"  :   "bot or not?show us your human side...we can't tell if you're a human or a bot.it seems we're having some difficulties. please give us a moment and try again.c5607da2-a94a-4300-ab77-a55fa90b7042",
    "regex"     :   "bot or not\?show us your human side",
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "bot protection          bot protection        you are seeing this because your ip was the source of too many requests.",
    "regex"     :   "bot protection\s{5,20}bot protection\s{5,20}you are seeing this because your ip was the source of too many requests",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "429 too many requests  too many requests the user has sent too many requests in a given amount of time.",
    "regex"     :   "429 too many requests\s{1,10}too many requests the user has sent too many requests in a given amount of time",
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "verifying if your connection is secure...        please turn on javascript and reload the page.             verifying if your connection is secure                   is protected by               deflect.ca  ddos protection for civil society",
    "regex"     :   "^verifying if your connection is secure\.\.\.\s{5,15}please turn on javascript and reload the page",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"deflect.ca"
})


refusal_regex_set.append({
	"full_msg"  :   "anti-crawler protection is activated for your ip  34.228.52.21 to continue working with the web site, please make sure that you have enabled javascript.   you will be automatically redirected to the requested page after 3 seconds.don't close this page. please, wait for 3 seconds to pass to the page.        the page was generated at thu, 07 dec 2023 12:31:46 browser time     959451, 13239,  https://digest.wizardsoft.ru, 5.159.1   antispam by cleantalk",
    #               "anti-crawler-schutz prüft deine(n) browser und ip 44.197.101.251 auf spam-bots um weiter auf der webseite zu arbeiten, stelle sicher, dass du javascript aktiviert hast.   du wirst automatisch nach 3 sekunden zur angeforderten seite weitergeleitet.diese seite nicht schließen. warte bitte 3 sekunden auf die seite.        the page was generated at thu, 07 dec 2023 10:29:54 browser time     958135, 12928,  https://www.alainveuve.ch, 6.15   anti-spam by cleantalk"
    "regex"     :   "^anti-crawler",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"cleantalk"
})

refusal_regex_set.append({
	"full_msg"  :   "la protection anti-crawler vérifie votre navigateur et votre adresse ip 3.239.2.192 contre les robots spameurs pour continuer à travailler avec le site, veuillez vous assurer que javascript est activé.   vous serez automatiquement redirigé vers la page demandée après 3 secondes.ne pas fermer cette page. patienter 3 secondes pour passer à la page.        the page was generated at mon, 11 dec 2023 11:40:03 browser time     1383773, 13671,  https://snbh.org, 6.23   anti-spam by cleantalk",
    "regex"     :   "^la protection anti-crawler vérifie votre navigateur",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"cleantalk"
})

refusal_regex_set.append({
	"full_msg"  :   "blacklisted                      der anti-crawler-schutz ist für deine ip aktiviert 18.206.12.157 um weiter auf der website zu arbeiten, stelle sicher, dass du javascript aktiviert hast.   du wirst automatisch nach 3 sekunden zur angeforderten seite weitergeleitet.diese seite nicht schließen. warte bitte 3 sekunden auf die seite.        the page was generated at sat, 09 dec 2023 08:12:34 browser time     915727, 13597,  https://www.cake-it-up.de, 5.154   anti-spam von cleantal",
    #               "blacklisted                      anti-crawler protection is activated for your ip  44.212.96.86 to continue working with the web site, please make sure that you have enabled javascript.   you will be automatically redirected to the requested page after 3 seconds.don't close this page. please, wait for 3 seconds to pass to the page.        the page was generated at sat, 09 dec 2023 23:37:48 browser time     858600, 13616,  https://www.quizammedia.com, 5.155   antispam by cleantalk"
    "regex"     :   "^blacklisted",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"cleantalk"
})
refusal_regex_set.append({
	"full_msg"  :   "spamfirewall is activated for your ip 34.228.52.21      to continue working with the web site, please make sure that you have enabled javascript.  please click the link below to pass the protection,   or you will be automatically redirected to the requested page after 3 seconds.        the page was generated at mon, 11 dec 2023 11:50:17 browser time     272512, 13758,  https://www.shomanstaffing.com, 5.157.2",
    "regex"     :   "^.{150,250}you will be automatically redirected to the requested page after",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"spamfirewall"
})
refusal_regex_set.append({
	"full_msg"  :   "just a moment...enable javascript and cookies to continue",
    "regex"     :   "^just a moment...enable javascript and cookies to continue",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"cloudflare"
})
refusal_regex_set.append({
	"full_msg"  :   "bot verification      to help us keep this website secure, please wait while we verify you're not a robot! it will only take a few seconds...  loading...",
    "regex"     :   "^bot verification",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "waiting for the redirectiron...          please, turn javascript on in your browser then reload the page.                 accessing /products/sportswear/ securely… this is an automatic process.  your browser will redirect to your requested content in 5 seconds.        security check by bitninja.io",
    "regex"     :   "^waiting for the redirect",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"bitninja"
})
refusal_regex_set.append({
	"full_msg"  :   "security testing        security testing in progress    click to go   supported by ï¼� guidechem copyright â© 2009 - . all rights reserved.",
    "regex"     :   "^security testing.{1,10}security testing in progress",
	"type"      :   "checking",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "infojobs                                ¿eres humano o un robot? hemos detectado una actividad poco habitual y necesitamos comprobar que no eres una máquina. disculpa las molestias.    más información ip: 44.220.249.141                nosotros  ayuda seguridad  condiciones legales  política de privacidad uso del servicio política de cookies gestionar publicidad       sobre infojobs  infojobs hoy trabaja con nosotros ofertas de empleo       + infojobs  infojobs academy orientación laboral infojobs formación blog empresas oferte di lavoro in italia       prensa  indicadores de infojobs notas de prensa contacto de prensa             ¡síguenos!                                         infojobs es parte de  adevinta  fotocasa habitaclia coches.net motos.net milanuncios jobisjob vibbo © adevinta spain s.l.u.",
    "regex"     :   "^infojobs\s{30,40}¿eres humano o un robot\?",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "access to this page has been blocked       please click and hold the button below to help us keep your account safe:   we need additional confirmation that you're human. this validation may be required as a result of the following: javascript is disabled or blocked by an extension (ad blockers for example), or your browser does not support cookies. if you are having problems accessing the site or need help, please contact us. please reference block id: #c9585e84-8e75-11ee-bffa-c894983992c5",
    "regex"     :   "^access to this page has been blocked.{50,100}we need additional confirmation that you're human",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "wexbo | firewallwww.krestanska-predajna.skz dôvodu prekročenia maximálneho limitu požiadaviek je nutné potvrdiť, že nie ste robot.",
    #               "wexbo | firewallwww.darkroseminiatures.combecause of exceeding the maximum requirement limit, you must confirm that you are not a robot.
	#"regex"     :   "^wexbo \| (ddos )?firewall.{1,100}dôvodu prekročenia maximálneho limitu požiadaviek je nutné potvrdiť, že nie ste robot",	
	"regex"     :   "^wexbo \| (ddos )?firewall.{1,150}robot",
    "type"      :   "challenge",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	"wexbo"
})
refusal_regex_set.append({
    #Exception: This was not identified by searching for keywords. Instead, it was added due to its high occurrence and as a result of manual investigation revealing that it was indeed a refusal page.
	"full_msg"  :   "not acceptable!not acceptable!an appropriate representation of the requested resource could not be found on this server. this error was generated by mod_security.",
	"regex"     :   "^not acceptable!not acceptable!an appropriate representation of the requested resource could not be found on this server\. this error was generated by mod_security",
    "type"      :   "block",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"modsecurity"
})
refusal_regex_set.append({
    #Exception: This was not identified by searching for keywords. Instead, it was added due to its high occurrence and as a result of manual investigation revealing that it was indeed a refusal page.
	"full_msg"  :   "error 403-notbranded occurred  regardless, we recommend you to update your browser.",
	"regex"     :   "^error 403-notbranded occurred",
    "type"      :   "block",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"wix" #found this by looking at the NS records of domains 
})

refusal_regex_set.append({
	"full_msg"  :   "oops..                        hmm, sorry but...          please complete the security check.  refresh image      continue  this security check has been powered by                        crowdsec",
    "regex"     :   "(fill( in| out)?|complete|solv(e)?)(ing)? (a|the|this)(below|following)? (security check|(re)?captcha|challenge)",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	"crowdsec"
})
refusal_regex_set.append({
	"full_msg"  :   "verificação de segurança      verificação de segurança complete o desafio abaixo para acessar alternativaimoveis.com            id da requisição: ab67807b34aca882fd57bb9536c98b94 - seu endereço ip: 151.139.21.8 horário: 2023-12-03 03:51:56 - local: 000  |",
    "regex"     :   "^verificação de segurança",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "(confirm|verify|prove) ((that )?you(.re| are) (not )?(a )?((ro)?bot|human)|it(.s| is) you)",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "(type|enter) the characters",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "(fill( in| out)?|complete|solv(e)?)(ing)? (a|the|this)(below|following)? (security check|(re)?captcha|challenge)",
	"type"      :   "challenge",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "(your )?ip( address)? (is|was|has been) (blocked|restricted|limited)",
	"type"      :   "block",
    "who"       :   "ip",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "(unusual|suspicious) (traffic|activity) (detected|seen)?(?!report)",
	"type"      :   "",
    "who"       :   "",
	"why"       :   "excessive/suspicious",
	"tag"		:	""
})
refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "(malicious|harmful|unsafe) (traffic|activity) (detected|seen)?(?!report)",
	"type"      :   "",
    "who"       :   "",
	"why"       :   "security/malicious",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "kompass.complease enable js and disable any ad blocker",
    "regex"     :   "^.{1,50}please enable js and disable any ad blocker",
	"type"      :   "require_js",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "security check      security check please turn javascript on and reload the page.please enable cookies and reload the page. requestor ip:  18.206.48.243  error ray id:  83312341992e82e7   we're sorry for the inconvenience but something about your request was flagged by our security system. if this is a persistent problem, please check out our faq for solutions to common issues here at the mindbody security faq.  if you still can't resolve, please email securityblock@mindbodyonline.com at mindbody and include the ip address and ray id above.  we'll help you troubleshoot the issue as soon as we are able.  thank you. - mindbody security operations note:  please avoid emailing screenshots of this error page.  for accurate and efficient help, simply select and copy the ip and ray id text.",
    "regex"     :   "^security check\s{1,100}security check please turn javascript on and reload the page",
	"type"      :   "require_js",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "access to this page has been denied                  your browser appears to have javascript disabled.for instructions on how to enable javascript please click here.if you have any issues, please contact us at challengehelp@humansecurity.com",
    "regex"     :   "^access to this page has been denied.{10,25}your browser appears to have javascript disabled",
	"type"      :   "require_js",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
    #Exception  :   Despite not being explicit enough, manual investigation showed that it was indeed a block page not a regular error page.
	"full_msg"  :   "your request has been blocked...",
    "regex"     :   "^your request has been blocked\.\.\.$",
    "type"      :   "block",
	"who"       :   "request",
	"why"       :   "",
	"tag"		:	""
})


refusal_regex_set.append({
	"full_msg"  :   "access blocked by the system firewallip18.207.160.97user-agentccbot/2.0 (https://commoncrawl.org/faq/)referer",
    "regex"     :   "^access blocked by the system firewallip",
	"type"      :   "block",
    "who"       :   "request",
	"why"       :   "",
	"tag"		:	""
})

refusal_regex_set.append({
	"full_msg"  :   "",
    "regex"     :   "^.{0,100}block(ed)? by (the|our|a)?\s?((system|web application) firewall|waf|security)",
	"type"      :   "block",
    "who"       :   "",
	"why"       :   "",
	"tag"		:	""
})



################################################
## NON BLOCKS - STANDARD ERRORS
################################################
nonrefusal_regex_set = []

# Blank
nonrefusal_regex_set.append({
    "regex"     :   "^$",
	"type"      :   -1,
})

# Bad request
nonrefusal_regex_set.append({
	"regex"		:	"400\s*bad request",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"^bad request",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"error 400 \(bad request\)",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"description: could not process this request\.$",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"invalid dynamic link - blocked we could not match param",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"^invalid request$",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"invalid url the requested",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"^400$",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"400\. that.s an error\.",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"^http status 400",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"the uri you submitted has disallowed characters",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"bad request",
	"type"		:	-400
})
nonrefusal_regex_set.append({
	"regex"		:	"please check for any errors in the address bar",
	"type"		:	-400
})

# Authentication or authorization
nonrefusal_regex_set.append({
	"regex"		:	"401 authorization required\s*401 authorization required",
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"401 unauthorized\s*proper authorization is required to access this resource.$", #password protected,
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"unauthorized access",
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"^authentication required",
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"you are not logged in",
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"you must be logged-in to",
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"please login again to access the site",
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"please login to view this page",
	"type"		:	-401
})
nonrefusal_regex_set.append({
	"regex"		:	"this server could not verify that you are authorized to access the document requested",
	"type"		:	-401
})

nonrefusal_regex_set.append({
	"regex"		:	"error 402: payment required",
	"type"		:	-402
})

# URL specific 403
nonrefusal_regex_set.append({
	"regex"		:	"you do(n.t| not) have permission to access this resource",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"don't have permission to access /.{5,400} on this server",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"the following file\(s\) have been blocked by the administrator",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"a page that you don't have permission",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"access is being denied for the webpage you requested on .{5,30}please try accessing the site home page",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"access to the specified resource has been forbidden",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"we are sorry but you do not have access to this page or resource",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"sorry, you are not allowed to preview drafts",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"nemáte oprávnenie otvárať náhľady konceptov",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"kein zugriff auf diese seite",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"the requested URL is temporarly blocked out on this server",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"you might not have the necessary permissions to display this resource",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"request denied you are forbidden from viewing that file or directory",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"block technical data\s*block reason: accessed a banned url",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"the website owner or its software configuration has forbidden access to the url you are trying to access",
	"type"		:	-403
})
nonrefusal_regex_set.append({
	"regex"		:	"the following file(s) have been blocked by the administrator",
	"type"		:	-403
})


# Not found
nonrefusal_regex_set.append({
	"regex"		:	"^not found",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"404.{1,5}not found",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"page (you ((a|we)re looking for|requested))?(not (found|available)|unavailable|no longer exists|(has been|was) ((re)?moved|deleted))",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"page does not exist",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"the file you're trying to access is not available",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"article unavailable",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"nicht gefunden werden",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"pagina no encontrada",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"página não encontrada",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"page non trouvée",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"página no encontrada",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"could not be found",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"posting has been deleted by its author",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"you are trying to access does not exist",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"die suche ergab keine genauen",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"404\s*not found",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"is no longer available",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"pagina.niet.beschikbaar",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"you requested was not found",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"页面未找到",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"(job|page) you are trying to (apply for|access) has been filled",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"the job you are trying to view has been",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"the role you are trying to apply for has been",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"the page you were looking for, couldn't be found",
	"type"		:	-404
})
nonrefusal_regex_set.append({
	"regex"		:	"la page demandée n'existe",
	"type"		:	-404
})


# Not acceptable
nonrefusal_regex_set.append({
	"regex"		:	"406 not acceptable\s*406 not acceptable",
	"type"		:	-406
})
nonrefusal_regex_set.append({
	"regex"		:	"^406 not acceptable$",
	"type"		:	-406
})
nonrefusal_regex_set.append({
	"regex"		:	"^not acceptable",
	"type"		:	-406
})

# 410 gone errors
nonrefusal_regex_set.append({
	"regex"		:	"gone error 54113 details",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"^the page you requested was removed",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"page you are looking for",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"410 deleted by author",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"inerror410the author deleted this",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"410 gone nginx",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"this site has been archived",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"gone. redirecting to",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"deaktiviert bzw. entfernt",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"anbieter deaktiviert bzw. entfernt",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"410 - contenu supprimé",
	"type"		:	-410
})
nonrefusal_regex_set.append({
	"regex"		:	"erreur 410 - contenu",
	"type"		:	-410
})



# 500 errors
nonrefusal_regex_set.append({
    "regex"     :   "(compilation|system|server|internal|software|unexpected|fatal|application|critical)\s?error\s?(was encountered|(has )?occured)",
	"type"		:	-500
})
nonrefusal_regex_set.append({
    "regex"     :   "(encountered|experiencing) (a )?technical (problem|difficult(y|ies))",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"failed to connect due to a temporary error",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"een kritieke fout voorgedaan",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"einen kritischen fehler auf", # a critical erro,
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"un error crítico en",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"error crítico en esta",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"eu une erreur critique",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"un errore critico sul tuo",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"the provided host name is not valid for this server",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"client browser does not accept the mime type",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"probeert het probleem z.s.m. op te lossen",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"there (was|has been|is) an error",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"there has been a critical error on this website",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"server error in '/'",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"500 internal server error",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"an internal error",
	"type"		:	-500
})

nonrefusal_regex_set.append({
	"regex"		:	"we (ran into|are having|have).{0,10}(problems|troubles)",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"error establishing a database connection",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"this error message is generated when",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"508 resource limit is reached",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"we seem to have hit a snag",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"we.re working on this problem",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"we.re working to restore all services",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"we are working hard to fix it",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"an unexpected database error occurred",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"exception caught",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"unable to connect to the database",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"server could not process your request",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"server too busy for this request",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"our website is currently down",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"be back soon",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"website temporary unavailable",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"site blocked\s*the site is currently unavailable we are sorry for the inconvenience",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"website is temporarily down",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"attempt to read property",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"the server is temporarily unable to service your request due to maintenance downtime or capacity problems",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"an appropriate representation of the requested resource",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"extracted source \(around line",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"server is busy",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"looks like something went wrong",
	"type"		:	-500
})
nonrefusal_regex_set.append({
	"regex"		:	"(server|website) encountered an unexpected error",
	"type"		:	-500
})


# 502
nonrefusal_regex_set.append({
	"regex"		:	"bad gateway",
	"type"		:	-502
})
nonrefusal_regex_set.append({
	"regex"		:	"502 bad gateway",
	"type"		:	-502
})

# Service or website being unavailable 503
nonrefusal_regex_set.append({
	"regex"		:	"website currently unavailable",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"^the service is unavailable\.$",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"503 service unavailable\s*503 service unavailable",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"service temporarily unavailable",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"undergoing .+ maintenance",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"scheduled maintenance",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"offline for maintenance",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"we are currently updating our site",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"maintenance mode",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"undergoing maintenance",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"this site is currently unavailable",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"sorry, this store is currently unavailable",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"503 service unavailable no server is available to handle this",
	"type"		:	-503
})
nonrefusal_regex_set.append({
	"regex"		:	"503 backend fetch failed",
	"type"		:	-503
})
 

# CDN related errors
nonrefusal_regex_set.append({
	"regex"		:	"unable to reach the origin server",
	"type"		:	-504
})
nonrefusal_regex_set.append({
	"regex"		:	"unable to reach the website.s origin server",
	"type"		:	-504
})
nonrefusal_regex_set.append({
	"regex"		:	"web server is down",
	"type"		:	-504
})
nonrefusal_regex_set.append({
	"regex"		:	"504 gateway time-out\s*504 gateway time-out",
	"type"		:	-504
})
nonrefusal_regex_set.append({
	"regex"		:	"the gateway did not receive a timely response",
	"type"		:	-504
})

# Bandwidth
nonrefusal_regex_set.append({
	"regex"		:	"509 bandwidth limit exceeded",
	"type"		:	-509
})

# Keywords of definitely non-blocking pages
nonrefusal_regex_set.append({
	"regex"		:	"^423 locked",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"error 409 conflict",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"page archived",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"if you see this page it is because you have reached the default website",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"die bewerbungsfrist für diese stelle ist bereits abgelaufen", #The application deadline for this position has already expire,
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"цена без учета ндс", #translation: price excluding va,
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"don't have an account\? register now",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"skip to (main )?content",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"already have an account\?",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"for a better experience, please enable javascript in your browser",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"questo cookie contiene i",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"under construction",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"accessing author info via link is forbidden",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"please renew your subscription",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"destination link was classified as spam",
	"type"		:	-800
})
nonrefusal_regex_set.append({
	"regex"		:	"ucoz blocking\s+website is blocked blocking reason:", #example: malware -- a hosting providers page as to why a site is blocke,
	"type"		:	-800
})

# Censorship or service being suspended
nonrefusal_regex_set.append({
	"regex"		:	"sorry, blocked\s+site is blocked", #russian censorship page
	"type"		:	-900
})
nonrefusal_regex_set.append({
	"regex"		:	"простите, но данный сайт заблокирован для посещений из российской федерации в соответствии с законодательством рф",
	"type"		:	-900
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? this website is unavailable for legal reasons", #such as copyright infringemen,
	"type"		:	-900
})
nonrefusal_regex_set.append({
	"regex"		:	"sorry, you have been blocked you are unable to access",
	"type"		:	-900
})
nonrefusal_regex_set.append({
	"regex"		:	"sorry, blocked\s*site is blocked$",
	"type"		:	-900
})
nonrefusal_regex_set.append({
	"regex"		:	"this website has been blocked",
	"type"		:	-900
})


# Cloudflare errors
nonrefusal_regex_set.append({
	"regex"		:	"cloudflare is currently unable to resolve your requested domain",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"that is on the cloudflare network\. an unknown error occurred while rendering the page",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? .+ cloudflare network. the host .+ resolved to an ip address that the owner of the website does not have access to",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? the web server reported a gateway time-out error",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"the host is configured as a cname across accounts on cloudflare, which is not allowed by cloudflare's security policy",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? the web server is not returning a connection\. as a result, the web page is not displaying",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? the origin web server timed out responding to this request",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"that is on the cloudflare network\. unfortunately, it is resolving to",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"that is on the cloudflare network\. the page could not be rendered due to a temporary fault",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"is configured as an argo tunnel, and cloudflare is currently unable to resolve it",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? the web server reported a bad gateway error",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"the page request was canceled because it took too long to complete",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? cloudflare is unable to establish an ssl connection to the origin server",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? the origin web server does not have a valid ssl certificate",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"what happened\? the origin web server is not reachable",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"there is an unknown connection issue between cloudflare and the origin web server. as a result, the web page can not be displayed",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"the initial connection between cloudflare's network and the origin web server timed out. as a result, the web page can not be displayed",
	"type"		:	-1000
})
nonrefusal_regex_set.append({
	"regex"		:	"the web server reported a gateway time-out error",
	"type"		:	-1000
})
  

for i, regex_set in enumerate(refusal_regex_set, start=1):
    regex_set["regex_id"] = i  # Adding a unique ID like regex_1, regex_2, etc.
