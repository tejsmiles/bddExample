
@when('i visit homepage')
def step(context):
   context.browser.get('https://hungryhouse.co.uk/')

@then('i should see this "The easy way to takeaway | hungryhouse"')
def step(context):
   assert context.browser.title == "The easy way to takeaway | hungryhouse"
