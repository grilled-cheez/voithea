import webview

urls = ['https://oaidalleapiprodscus.blob.core.windows.net/private/org-6AWD8REcAL8pDtGKxD6aVcEh/user-vuqarrpfFrNeMEj6XCRomxho/img-LBvk1pmYqqZ0QWT3wIOmk20m.png?st=2023-03-13T13%3A03%3A53Z&se=2023-03-13T15%3A03%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-13T12%3A52%3A02Z&ske=2023-03-14T12%3A52%3A02Z&sks=b&skv=2021-08-06&sig=LpAK0MWBZSdAhErZ4c16jldFtKwaeMi%2BXXBPtbeKNNo%3D', 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-6AWD8REcAL8pDtGKxD6aVcEh/user-vuqarrpfFrNeMEj6XCRomxho/img-Vjwn5M1PuSF5G4AqigyPOaPE.png?st=2023-03-13T13%3A03%3A53Z&se=2023-03-13T15%3A03%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-13T12%3A52%3A02Z&ske=2023-03-14T12%3A52%3A02Z&sks=b&skv=2021-08-06&sig=8ExHE5lwx6xXTRMBjhYRjnHPYJnUUZCRkSSm87Yq1nA%3D', 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-6AWD8REcAL8pDtGKxD6aVcEh/user-vuqarrpfFrNeMEj6XCRomxho/img-YUvDyYb0rWW8GbsQcUatWufo.png?st=2023-03-13T13%3A03%3A53Z&se=2023-03-13T15%3A03%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-13T12%3A52%3A02Z&ske=2023-03-14T12%3A52%3A02Z&sks=b&skv=2021-08-06&sig=eYwZQ1hxTfg4TPGSNXXWppU4BeJGK5aPcIOqH9Sgt0c%3D',
        'https://oaidalleapiprodscus.blob.core.windows.net/private/org-6AWD8REcAL8pDtGKxD6aVcEh/user-vuqarrpfFrNeMEj6XCRomxho/img-I44H3jJCMsuOEobijnnsDFFB.png?st=2023-03-13T13%3A03%3A53Z&se=2023-03-13T15%3A03%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-13T12%3A52%3A02Z&ske=2023-03-14T12%3A52%3A02Z&sks=b&skv=2021-08-06&sig=SIffZpD0YMw0%2BeIOo83/ifvh6CVxNmhWnwQPK/wIiQg%3D', 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-6AWD8REcAL8pDtGKxD6aVcEh/user-vuqarrpfFrNeMEj6XCRomxho/img-kk1aHwflIwYAVN7wvXk69AGO.png?st=2023-03-13T13%3A03%3A54Z&se=2023-03-13T15%3A03%3A54Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-03-13T12%3A52%3A02Z&ske=2023-03-14T12%3A52%3A02Z&sks=b&skv=2021-08-06&sig=e3QOrDM%2BTE6%2BbHCOKulhKtWtZwZPKMUNl%2BGlT1RHYBU%3D']
h = 0
w = 0
# def dall_e_layout(urls):  # function takes the list of urls of the generated images and produces a well laid output requires an index.txt file and an empty index.html file
f = open('index.txt', 'r+')
webpage = open('index.html', 'w+')
webcode = f.read()
num = len(urls)

if num <= 2:
    w1 = 1
elif 2 < num <= 4:
    w1 = 2
else:
    w1 = 3

h = 730
w = 1.035 * w1 * 341
if '<div class="container">' in webcode:
    ind = webcode.index('<div class="container">') + \
        len('<div class="container">')
    for i in range(0, len(urls), 2):
        image_design = ''
        image_design = image_design + \
            f'<div class="image"> <img src="{urls[i]}" height="341px" width="341px"/> </div> '
        webcode = webcode[:ind] + image_design + webcode[ind:]
    ind1 = webcode.index('<div class="container1">') + \
        len('<div class="container1">')
    for i in range(1, len(urls), 2):
        image_design = ''
        image_design = image_design + \
            f'<div class="image"> <img src="{urls[i]}" height="341px" width="341px"/> </div> '
        webcode = webcode[:ind1] + image_design + webcode[ind1:]

webpage.write(webcode)
webpage.close()
window = webview.create_window(
    'Images', 'index.html', width=int(w*1.26), height=int(h*1.28))
webview.start()
print(f"H is {int(h)}, w is {int(w)}")
# width=w, height=h
