from pupa.scrape import Scraper, Legislator, Committee
import lxml.html


class PersonScraper(Scraper):

    def lxmlize(self, url):
        entry = self.urlopen(url)
        page = lxml.html.fromstring(entry)
        page.make_links_absolute(url)
        return page

    def get_people(self):
        url = 'http://www.cabq.gov/council/councilors'
        page = self.lxmlize(url)
        names = page.xpath("//div[@id='parent-fieldname-text']/*")[3:]
        it = iter(names)
        for entry in zip(it, it, it):
            name, info, _ = entry
            image_small = name.xpath(".//img")[0].attrib['src']
            name = name.text_content()
            infopage, email, policy_analyst = info.xpath(".//a")
            phone = info.xpath(".//b")[-1].tail.strip()
            district = infopage.text_content()
            homepage = self.lxmlize(infopage.attrib['href'])
            photo = homepage.xpath(
                "//div[@class='featureContent']//img"
            )[0].attrib['src']

            bio = "\n".join((x.text_content() for x in homepage.xpath(
                "//div[@class='featureContent']//div[@class='stx']/p")))

            p = Legislator(name=name,
                           post_id=district,
                           image=photo,
                           biography=bio)

            p.add_source(url)
            p.add_source(infopage.attrib['href'])
            yield p
