class IntentExamples:
    # all examples are stored in lists
    hour_info = [
         "Are you open on Christmas' Day?",
         'Are you open on Saturdays?',
         'Are you open on Sundays?',
         'what are the hours of operation for your Montreal store',
         'what are you hours of operation in Toronto',
         'What are your hours?',
         'What are your hours of operation?',
         'What days are you closed on?',
         'What time are you open until?',
         'When are you open',
         'When do you close',
         'When do you open'
        ]
    location_info = [
         'do you have a flower shop in Montreal',
         'Give me a list of locations',
         'List of location',
         'list of your locations',
         'locations in America',
         'Locations in Canada',
         'What are your locations?',
         "What's the address of your Toronto store?",
         "what's the address of your Vancouver store?",
         'Where are you physically located?',
         'Where are your stores?',
         'where is your Toronto store?'
    ]


class EntityValues:
    # all values are stored in lists
    # the first value in a list is the key value
    # the remaining values are symptoms

    location = [('Mid Glamorgan', ['Aberdare', 'Bridgend', 'Caerphilly', 'Maesteg', 'Merthyr Tydfil', 'Pontyclun', 'Pontypridd', 'Porthcawl']), ('Aberdeenshire', ['Aberdeen', 'Banff', 'Ellon', 'Fraserburgh', 'Huntly', 'Insch', 'Inverurie', 'Maud', 'Peterhead', 'Turriff']), ('Gwynedd', ['Aberdovey', 'Arthog', 'Bala', 'Bangor', 'Barmouth', 'Beaumaris', 'Blaenau Ffestiniog', 'Caernarvon', 'Cemmaes Bay', 'Cemmaes Road', 'Conwy', 'Dolgellau', 'Holyhead', 'Llanbedr', 'Llandudno', 'Llanrwst', 'Nefyn', 'Penmaenmawr', 'Penrhyndeudraeth', 'Porthmadog', 'Pwllheli', 'Talybont', 'Tywyn']), ('Gwent', ['Abergavenny', 'Abertillery', 'Chepstow', 'Cwmbran', 'Ebbw Vale', 'Monmouth', 'Tredegar']), ('Clwyd', ['Abergele', 'Colwyn Bay', 'Corwen', 'Deeside', 'Flint', 'Llangollen', 'Mold', 'Prestatyn', 'Rhyl', 'Ruthin', 'St Asaph', 'Wrexham']), ('Dyfed', ['Aberystwyth', 'Cardigan', 'Carmarthen', 'Fishguard', 'Llandysul', 'Llanelli', 'Llanwrda', 'Newcastle Emlyn', 'Pembroke', 'Tenby', 'Whitland']), ('Oxfordshire', ['Abingdon', 'Banbury', 'Bicester', 'Chipping Norton', 'Didcot', 'Faringdon', 'Henley-on-Thames', 'Oxford', 'Thame', 'Wallingford', 'Wantage', 'Witney']), ('Lancashire', ['Accrington', 'Blackburn', 'Blackpool', 'Bolton', 'Burnley', 'Bury', 'Carnforth', 'Chorley', 'Clitheroe', 'Coppull', 'Fleetwood', 'Garstang', 'Heywood', 'Hornby', 'Lancaster', 'Leigh', 'Leyland', 'Littleborough', 'Lytham StAnnes', 'Morecambe', 'Nelson', 'Oldham', 'Ormskirk', 'Poulton-le-Fylde', 'Preston', 'Rochdale', 'Rossendale', 'Salford', 'Skelmersdale', 'Wigan']), ('Lanarkshire', ['Airdrie', 'Biggar', 'Carluke', 'Coatbridge', 'Lanark', 'Motherwell', 'Wishaw']), ('Warwickshire', ['Alcester', 'Coleshill', 'Kenilworth', 'Lapworth', 'Leamington Spa', 'Nuneaton', 'Rugby', 'Southam', 'Stratford-upon-Avon', 'Warwick', 'Warwickshire']), ('Suffolk', ['Aldeburgh', 'Beccles', 'Bungay', 'Bury St Edmunds', 'Felixstowe', 'Haverhill', 'Ipswich', 'Leiston', 'Lowestoft', 'Mildenhall', 'Newmarket', 'Pakenham', 'Saxmundham', 'Stowmarket', 'Sudbury']), ('Cheshire', ['Alderley Edge', 'Altrincham', 'Cheadle', 'Chester', 'Congleton', 'Crewe', 'Ellesmere Port', 'Holmes Chapel', 'Hyde', 'Knutsford', 'Macclesfield', 'Malpas', 'Middlewich', 'Nantwich', 'Northwich', 'Runcorn', 'Sandbach', 'Stockport', 'Tarporley', 'Warrington', 'Wilmslow']), ('Hampshire', ['Aldershot', 'Alresford', 'Alton', 'Andover', 'Basingstoke', 'Bishops Waltham', 'Bordon', 'Brockenhurst', 'Eastleigh', 'Emsworth', 'Fareham', 'Farnborough', 'Fleet', 'Gosport', 'Havant', 'Hayling Island', 'Hook', 'Liphook', 'Liss', 'Lymington', 'Lyndhurst', 'Petersfield', 'Portsmouth', 'Ringwood', 'Rockbourne', 'Romsey', 'Southampton', 'Southsea', 'Winchester']), ('Derbyshire', ['Alfreton', 'Ashbourne', 'Buxton', 'Chesterfield', 'Derby', 'Glossop', 'Hathersage', 'Heanor', 'Ilkeston', 'Matlock', 'New Mills', 'Ripley']), ('Ross-shire', ['Alness', 'Dingwall', 'Fortrose', 'Gairloch', 'Kyle', 'Lochcarron', 'Strathcarron', 'Strathpeffer', 'Tain']), ('Northumberland', ['Alnwick', 'Ashington', 'Bamburgh', 'Berwick-on-Tweed', 'Corbridge', 'Cramlington', 'Haltwhistle', 'Hexham', 'Kirkwhelpington', 'Prudhoe', 'Riding Mill', 'Rothbury', 'Seahouses', 'Stocksfield']), ('Cumbria', ['Alston', 'Ambleside', 'Appleby-in-Westmorland', 'Barrow-in Furness', 'Brampton', 'Carlisle', 'Cockermouth', 'Coniston', 'Gosforth', 'Grange-over-Sands', 'Hawkshead', 'Kendal', 'Keswick', 'Kirkby Stephen', 'Maryport', 'Penrith', 'Pooley Bridge', 'Raughton Head', 'Sedbergh', 'Shap', 'Ulverston', 'Whitehaven', 'Wigton', 'Windermere', 'Workington']), ('Buckinghamshire', ['Amersham', 'Aylesbury', 'Buckingham', 'Chesham', 'Gerrards Cross', 'Great Missenden', 'High Wycombe', 'Marlow', 'Milton Keynes', 'Newport Pagnell', 'Princes Risborough']), ('Wiltshire', ['Amesbury', 'Calne', 'Chippenham', 'Devizes', 'Malmesbury', 'Marlborough', 'Melksham', 'Mere', 'Pewsey', 'Salisbury', 'Shaftesbury', 'Swindon', 'Trowbridge', 'Warminster', 'Westbury']), ('Carmarthenshire', ['Ammanford', 'Llandeilo', 'Llandovery', 'St Clears']), ('Fife', ['Anstruther', 'Cupar', 'Dunfermline', 'Glenrothes', 'Kirkcaldy', 'St Andrews']), ('Co Antrim', ['Antrim', 'Ballycastle', 'Ballyclare', 'Ballymena', 'Ballymoney', 'Bushmills', 'Carrickfergus', 'Crumlin', 'Lisburn', 'Lurgan', 'Newtownabbey', 'Portrush']), ('Angus', ['Arbroath', 'Dundee', 'Forfar', 'Kirriemuir', 'Montrose']), ('Ayrshire', ['Ardrossan', 'Ayr', 'Dalry', 'Darvel', 'Kilbirnie', 'Kilmarnock', 'Prestwick', 'Saltcoats', 'West Kilbride']), ('Co Armagh', ['Armagh', 'Craigavon']), ('West Sussex', ['Arundel', 'Billingshurst', 'Bognor Regis', 'Burgess Hill', 'Chichester', 'Crawley', 'East Grinstead', 'Hassocks', 'Haywards Heath', 'Henfield', 'Horsham', 'Lancing', 'Littlehampton', 'Midhurst', 'Petworth', 'Pulborough', 'Worthing']), ('Berkshire', ['Ascot', 'Bracknell', 'Hungerford', 'Maidenhead', 'Newbury', 'Reading', 'Sandhurst', 'Slough', 'Thatcham', 'Windsor', 'Wokingham']), ('Devon', ['Ashburton', 'Axminster', 'Bamstaple', 'Barnstaple', 'Bideford', 'Braunton', 'Brixham', 'Buckfastleigh', 'Budleigh Salterton', 'Crediton', 'Cullompton', 'Exeter', 'Exmouth', 'Holsworthy', 'Honiton', 'Ilfracombe', 'Kingsbridge', 'Lynton', 'Moretonhampstead', 'Newton Abbot', 'Okehampton', 'Paignton', 'Plymouth', 'Seaton', 'Sidmouth', 'South Molton', 'Tavistock', 'Teignmouth', 'Tiverton', 'Torquay', 'Torrington', 'Umberleigh', 'Yelverton']), ('Middlesex', ['Ashford', 'Brentford', 'Edgware', 'Enfeld', 'Greenford', 'Hampton', 'Harrow', 'Hayes', 'Hounslow', 'Isleworth', 'Northwood', 'Pinner', 'Ruislip', 'Shepperton', 'Southall', 'Staines', 'Stanmore', 'Sunbury-on-Thames', 'Teddington', 'Twickenham', 'Uxbridge', 'Wembley', 'West Drayton']), ('Surrey', ['Ashtead', 'Banstead', 'Camberley', 'Carshalton', 'Caterham', 'Cheam', 'Chertsey', 'Cobham', 'Coulsdon', 'Cranleigh', 'Croydon', 'Dorking', 'East Molesey', 'Egham', 'Epsom', 'Esher', 'Farnham', 'Godalming', 'Godstone', 'Guildford', 'Haslemere', 'Hindhead', 'Horley', 'Kingston upon Thames', 'Leatherhead', 'Lightwater', 'Lingfield', 'Mitcham', 'Morden', 'New Malden', 'Oxted', 'Purley', 'Redhill', 'Reigate', 'Richmond', 'South Croydon', 'Surbiton', 'Sutton', 'Thornton Heath', 'Wallington', 'Walton-on-Thames', 'West Byfleet', 'Weybridge', 'Woking', 'Yateley']), ('Greater Manchester', ['Ashton-under-Lyne', 'Manchester']), ('Norfolk', ['Attleborough', 'Brooke', 'Cromer', 'Dereham', 'Diss', 'Downham Market', 'Fakenham', 'Great Yarmouth', 'Holt', 'Hunstanton', "King's Lynn", 'North Walsham', 'Norwich', 'Sheringham', 'Swaffham', 'Thetford', 'Walsingham', 'Wells-next-the-Sea', 'Wymondham']), ('Inverness-shire', ['Aviemore', 'Croy', 'Fort William', 'Inverness', 'Kingussie', 'Nairn', 'Nethy Bridge']), ('Hertfordshire', ['Baldock', 'Barnet', 'Berkhamsted', "Bishop's Stortford", 'Borehamwood', 'Harpenden', 'Hatfield', 'Hemel Hempstead', 'Hertford', 'Hitchin', 'Hoddesdon', 'Kings Langley', 'Letchworth', 'Potters Bar', 'Radlett', 'Rickmansworth', 'Royston', 'Sawbridgeworth', 'St Albans', 'Stevenage', 'Tring', 'Waltham Cross', 'Ware', 'Watford', 'Welwyn', 'Welwyn Garden City']), ('Argyll', ['Ballachulish', 'Campbeltown', 'Dalmally', 'Dunoon', 'Inveraray', 'Lochgilphead', 'Oban', 'Tarbert']), ('Co Down', ['Banbridge', 'Castlewellan', 'Downpatrick', 'Dromore', 'Hillsborough', 'Holywood', 'Newtownards']), ('Kincardineshire', ['Banchory', 'Stonehaven']), ('Essex', ['Barking', 'Basildon', 'Benneet', 'Billericay', 'Braintree', 'Brentwood', 'Buckhurst Hill', 'Chelmsford', 'Clacton-on-Sea', 'Colchester', 'Dagenham', 'Dunmow', 'Epping', 'Frinton-on-Sea', 'Grays Thurrock', 'Great Dunmow', 'Halstead', 'Harlow', 'Harwich', 'Hockley', 'Hornchurch', 'Ilford', 'Ingatestone', 'Laindon', 'Leigh-on-Sea', 'Loughton', 'Maldon', 'Ongar', 'Rayleigh', 'Rochford', 'Romford', 'Saffron Walden', 'Southend-on-Sea', 'Southminster', 'Stanford-le-Hope', 'Tilbury', 'Walton on the Naze', 'Westcliff-on-Sea', 'Wickford', 'Witham', 'Woodford Green']), ('Co Durham', ['Barnard Castle', 'Bishop Auckland', 'Chester-le-Street', 'Consett', 'Darlington', 'Durham', 'Seaham', 'Sedgefield']), ('South Yorkshire', ['Barnsley', 'Doncaster', 'Mexborough', 'Rotherham', 'Sheffield']), ('South Glamorgan', ['Barry', 'Cardiff', 'Dinas Powis', 'Llantwit', 'Penarth']), ('South Humberside', ['Barton-upon-Humber', 'Cleethorpes', 'Grimsby', 'Immingham', 'Scunthorpe']), ('Avon', ['Bath', 'Bristol', 'Clevedon', 'Nailsea', 'Weston-super-Mare']), ('West Lothian', ['Bathgate', 'Botness', 'Broxburn', 'Livingston', 'South Queensferry']), ('East Sussex', ['Battle', 'Bexhill-on-Sea', 'Brighton', 'Crowborough', 'Eastbourne', 'Hailsham', 'Hastings', 'Heathfield', 'Hove', 'Lewes', 'Newhaven', 'Pevensey', 'Robertsbridge', 'Rye', 'Seaford', 'St Leonards-on-Sea', 'Uckfield']), ('Kent', ['Beckenham', 'Belvedere', 'Broadstairs', 'Bromley', 'Canterbury', 'Chatham', 'Cranbrook', 'Dartford', 'Deal', 'Dover', 'Ebbsfleet', 'Edenbridge', 'Erith', 'Folkestone', 'Gillingham', 'Gravesend', 'Herne Bay', 'Hythe', 'Maidstone', 'Margate', 'Medway', 'Orpington', 'Ramsgate', 'Rochester', 'Sandwich', 'Sevenoaks', 'Sidcup', 'Sittingbourne', 'Swanley', 'Thanet', 'Tonbridge', 'Tunbridge Wells', 'Welling', 'West Malling', 'West Wickham', 'Westerham', 'Whitstable']), ('North Yorkshire', ['Bedale', 'Easingwold', 'Guisborough', 'Harrogate', 'Helmsley', 'Leyburn', 'Malton', 'Northallerton', 'Pickering', 'Ripon', 'Scarborough', 'Selby', 'Settle', 'Skipton', 'Sowerby', 'Thirsk', 'West Heslerton', 'Whitby', 'York']), ('Bedfordshire', ['Bedford', 'Biggleswade', 'Dunstable', 'Leighton Buzzard', 'Luton', 'Sandy']), ('Belfast', ['Belfast', 'Dunmurry']), ('Conwy', ['Betws-y-Coed']), ('North Humberside', ['Beverley', 'Bridlington', 'Driffield', 'Hessle', 'Hull']), ('Worcestershire', ['Bewdley', 'Evesham']), ('West Yorkshire', ['Bingley', 'Bradford', 'Brighouse', 'Dewsbury', 'Guiseley', 'Halifax', 'Huddersfield', 'Ilkley', 'Keighley', 'Leeds', 'Mirfield', 'Ossett', 'Otley', 'Pontefract', 'Shipley', 'Wakefield', 'Wetherby']), ('Merseyside', ['Birkenhead', 'Bootle', 'Liverpool', 'Newtown-le- Willows', 'Prescot', 'South Wirral', 'Southport', 'St Helens', 'Wallasey', 'Wirral']), ('West Midlands', ['Birmingham', 'Coventry', 'Dudley', 'Halesowen', 'Kingswinford', 'Meriden', 'Solihull', 'Stourbridge', 'Sutton Coldfield', 'Tipton', 'Walsall', 'Warley', 'West Bromwich', 'Wolverhampton']), ('Shropshire', ['Bishops Castle', 'Bridgnorth', 'Church Stretton', 'Craven Arms', 'Ironbridge', 'Ludlow', 'Market Drayton', 'Newport', 'Oswestry', 'Shifnal', 'Shrewsbury', 'Telford', 'Wem', 'Whitchurch']), ('Perthshire', ['Blairgowrie', 'Crieff', 'Dunblane', 'Dunkeld', 'Killin', 'Perth', 'Pitlochry']), ('Dorset', ['Blandford Forum', 'Bournemouth', 'Bridport', 'Cerne Abbas', 'Christchurch', 'Dorchester', 'Poole', 'Sherborne', 'Swanage', 'Wareham', 'Weymouth', 'Wimborne']), ('Tyne and Wear', ['Blaydon-on-Tyne', 'Boldon Colliery', 'Gateshead', 'Houghton le Spring', 'Newcastle upon Tyne', 'North Shields', 'Ryton', 'Sunderland', 'Washington', 'Whitley Bay']), ('Cornwall', ['Bodmin', 'Bude', 'Camelford', 'Falmouth', 'Fowey', 'Helston', 'Launceston', 'Liskeard', 'Newquay', 'Par', 'Penryn', 'Penzance', 'Port Isaac', 'Redruth', 'Saltash', 'St Austell', 'St Ives', 'Truro', 'Wadebridge']), ('Midlothian', ['Bonnyrigg', 'Grangemouth', 'Loanhead', 'Musselburgh', 'Penicuik']), ('Lincolnshire', ['Boston', 'Bourne', 'Brigg', 'Gainsborough', 'Grantham', 'Holbeach', 'Honington', 'Killingholme', 'Lincoln', 'Louth', 'Market Rasen', 'Martin', 'Skegness', 'Sleaford', 'Spalding', 'Spilsby', 'Stamford']), ('Northamptonshire', ['Brackley', 'Clopton', 'Corby', 'Daventry', 'Kettering', 'Northampton', 'Rushden', 'Towcester', 'Wellingborough']), ('Powys', ['Brecon', 'Builth Wells', 'Hay-on-Wye', 'Knighton', 'Llandrindod Wells', 'Llanidloes', 'Llanwrtyd Wells', 'Machynlleth', 'Meifod', 'Montgomery', 'Newtown', 'Welshpool']), ('Somerset', ['Bridgwater', 'Burnham-on-Sea', 'Chard', 'Cheddar', 'Dulverton', 'Frome', 'Glastonbury', 'Highbridge', 'Minehead', 'Shepton Mallet', 'South Petherton', 'Street', 'Taunton', 'Temple Cloud', 'Templecombe', 'Watchet', 'Wedmore', 'Wells', 'Wincanton', 'Winscombe', 'Yeovil']), ('Isle of Skye', ['Broadford', 'Kyleakin', 'Portree']), ('Hereford and Worcester', ['Broadway', 'Bromsgrove', 'Droitwich', 'Hereford', 'Kidderminster', 'Ledbury', 'Leominster', 'Malvern', 'Pershore', 'Stourport-on-Severn', 'Worcester']), ('Isle of Arran', ['Brodick']), ('Banffshire', ['Buckie']), ('Isle of Mull', ['Bunessan']), ('Staffordshire', ['Burton-on-Trent', 'Cannock', 'Ipstones', 'Lichfield', 'Newcastle', 'Rugeley', 'Stafford', 'Stoke-on-Trent', 'Stone', 'Tamworth', 'Uttoxeter']), ('Cambridgeshire', ['Cambridge', 'Chatteris', 'Ely', 'Huntingdon', 'Madingley', 'March', 'Peterborough', 'Warboys', 'Wisbech']), ('Isle of Lewis', ['Carloway', 'Shawbost', 'Stornoway']), ('Kirkcudbrightshire', ['Castle Douglas', 'Dalbeattie']), ('Co Tyrone', ['Castlederg', 'Clogher', 'Cookstown', 'Dungannon', 'Fivemiletown', 'Omagh']), ('Isle of Man', ['Castletown', 'Douglas', 'Ramsey']), ('Gloucestershire', ['Cheltenham', 'Chipping Sodbury', 'Cirencester', 'Dursley', 'Gloucester', 'Lydney', 'Mitcheldean', 'Newent', 'Stow-on-the-Wold', 'Stroud', 'Tewkesbury', 'Wotton-under-Edge']), ('Gloucestershne', ['Cinderford']), ('Leicestershire', ['Coalville', 'Hinckley', 'Leicester', 'Loughborough', 'Lutterworth', 'Market Harborough', 'Melton Mowbray', 'Oakham']), ('Co Londonderry', ['Coleraine', 'Limavady', 'Londonderry', 'Magharafelt']), ('East Ayrshire', ['Cumnock', 'Moscow']), ('Sutherland', ['Dornoch', 'Lairg']), ('Dunbartonshire', ['Dumbarton', 'Helensburgh']), ('Dumfriesshire', ['Dumfries', 'Gretna', 'Lockerbie', 'Sanquhar']), ('East Lothian', ['Dunbar', 'Gullane', 'Haddington', 'North Berwick', 'Tranent']), ('Berwickshire', ['Duns']), ('South Lanarkshire', ['East Kilbride', 'Strathaven']), ('Edinburgh', ['Edinburgh']), ('Morayshire', ['Elgin']), ('Co Fermanagh', ['Enniskillen']), ('Stirlingshire', ['Falkirk', 'Larbert', 'Stirling']), ('Isle of Wight', ['Freshwater', 'Isle of Wight', 'Sandown', 'Totland Bay', 'Ventnor']), ('Selkirkshire', ['Galasheils', 'Selkirk']), ('South Ayrshire', ['Girvan']), ('Rotherham', ['Glamorgan']), ('Glasgow', ['Glasgow']), ('East Riding of Yorkshire', ['Goole', 'Hornsea', 'Market Weighton', 'Pocklington']), ('Renfrewshire', ['Greenock', 'Johnstone', 'Kilmacolm', 'Lochwinnoch', 'Paisley']), ('Channel Islands', ['Guernsey', 'Jersey']), ('Lanark shire', ['Hamilton']), ('Cleveland', ['Hartlepool', 'Middlesbrough', 'Redcar', 'Saltburn-by-the-Sea', 'Stockton-on-Tees']), ('Pembrokeshire', ['Haverfordwest', 'Milford Haven', 'Narberth']), ('Roxburghshire', ['Hawick', 'Kelso', 'Newcastleton']), ('Isle of Iona', ['Iona']), ('Herefordshire', ['Kington', 'Pencombe', 'Ross-on-Wye', 'Wormbridge']), ('Ceredigion', ['Lampeter', 'Llanarth', 'Llanon']), ('Caithness', ['Latheron', 'Thurso', 'Wick']), ('Isle of Shetland', ['Lerwick', 'Shetland']), ('Isle of Uist', ['Lochboisdale']), ('London', ['London']), ('Nottinghamshire', ['Mansfield', 'Newark', 'Nottingham', 'Nottinghamshire', 'Southwell', 'Sutton-in-Ashfield', 'Whatton', 'Worksop']), ('Northumberiand', ['Morpeth']), ('Neath Port Talbot', ['Neath']), ('Torfaen', ['Pontypool']), ('West Glamorgan', ['Port Talbot', 'Swansea']), ('&nbsp;', ['No Entries']), ('Hereford and', ['Redditch']), ('Nottmghamshire', ['Retford']), ('Isle ofBute', ['Rothesay']), ('Isle of Tiree', ['Scarinish']), ('Wigtownshire', ['Stranraer']), ('Peeblesshire', ['West Linton'])]