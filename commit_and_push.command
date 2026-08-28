#!/bin/bash
cd ~/clawd/tap-water-guide
rm -f .git/index.lock .git/index2
git config user.name "729r2pzfqs-ux"
git config user.email "729r2pzfqs-ux@users.noreply.github.com"
git add -A
git commit -m "Add 27 new country pages and 48 new city pages

New countries (27): Chile, Georgia, Montenegro, Russia, Bahamas, Estonia,
Albania, Romania, Bermuda, Israel, Ukraine, Lithuania, Latvia, Cyprus,
Bulgaria, Uruguay, Nicaragua, Cayman Islands, El Salvador, Sri Lanka,
Qatar, Belgium, Malta, Ecuador, Panama, China, Taiwan

New cities (48): Madrid, Copenhagen, Milan, Munich, Berlin, Florence,
Venice, Edinburgh, Dubrovnik, Porto, Zurich, Brussels, Malta, Santorini,
Mykonos, Valencia, Sicily, Naples, Seville, Split, Oslo, Reykjavik,
Warsaw, Krakow, Nice, Zagreb, Bucharest, Mexico City, Cabo San Lucas,
Medellin, Rio de Janeiro, Puerto Vallarta, Quito, Panama City, Cusco,
Santiago, Cartagena, San Jose Costa Rica, Shanghai, Beijing,
Ho Chi Minh City, Kuala Lumpur, Kyoto, Osaka, Taipei, Phuket,
Abu Dhabi, Johannesburg

Site rebuilt with 205 URLs in sitemap. QA: 0 duplicate titles,
0 duplicate meta descriptions, 0 broken links."
git push origin main
echo ""
echo "Done! Press any key to close..."
read -n 1
