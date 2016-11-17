# Singkep Island Open Dataset

Collection of open dataset about Singkep Island.

## About Singkep Island

Singkep Island is one of the island in Lingga Archipelago, Indonesia. Located in
east of Sumatera, Singkep is one of major island in Lingga Regency. Singkep have
land area of 757 square kilometers (292 sq mi.) and population of 22.094 person
(2014). Tourism from it's beautiful beach is a major activity in Singkep island.
(taken from [Wikipedia Indonesia](https://id.wikipedia.org/wiki/Pulau_Singkep))

| Data | Value |
|------|----|
| Name | Pulau Singkep |
| Provinsi | Riau |
| Kabupaten | Lingga |
| Wikipedia | <https://id.wikipedia.org/wiki/Pulau_Singkep> |
| Wikidata  | <https://www.wikidata.org/wiki/Q2093843> |
| Population | 22.094 (2014) |


## Provided Dataset

All data is in GeoJson format, separated in different file.


### [Singkep Island coastline, mountain, and major settlement/village]

All data taken from Openstreetmap via overpass API.

File:
- [Singkep coastline](https://github.com/BesutKode/uni-task-2-adhikasp/blob/master/data/singkep-coastline.geojson)
- [Singkep mountain](https://github.com/BesutKode/uni-task-2-adhikasp/blob/master/data/singkep-mountain.geojson)
- [Singkep village](https://github.com/BesutKode/uni-task-2-adhikasp/blob/master/data/singkep-village.geojson)

**License** under [Open Data Commons Open Database License (ODbL)](http://opendatacommons.org/licenses/odbl/)

### [Kecamatan/county Administrative region](https://github.com/BesutKode/uni-task-2-adhikasp/blob/master/data/singkep-administrative.geojson)

All data taken from map provided in regional statistic record by BPS
(Badan Pusat Statistik) Kabupaten Lingga. Traced manually from image file
(see `references` folder for the png file).

This is the source for the statistic document file.
- [Singkep Barat Statistic 2016](https://linggakab.bps.go.id/index.php/publikasi/149)
- [Singkep Selatan Statistic 2016](https://linggakab.bps.go.id/index.php/publikasi/146)
- [Singkep Pesisir Statistic 2016](https://linggakab.bps.go.id/index.php/publikasi/147)
- [Singkep Statistic](https://linggakab.bps.go.id/index.php/publikasi/148)

**License** by [Badan Pusat Statistika Lingga](https://linggakab.bps.go.id), all
right reserved.

**Warning**  
This county borderline is traced manually thus the resulting map is not precise,
just generally matching.  
Also, I do not find explicit data about Kecamatan Singkep region map. The
statistic data only provide old map. The area I create is based on area NOT
included in other Kecamatan region.

A maybe a little relevant news link
- <http://batamtoday.com/berita54944-Pemekaran-Kabupaten-Kepulauan-Singkep-Tunggu-Rekomendasi-dari-Gubernur-Kepri.html>.
- <http://selingga.com/799/>

### [Forest critical land area](https://github.com/BesutKode/uni-task-2-adhikasp/blob/master/data/singkep-lahan-kritis.geojson)

Data provided from Dinas Kehutanan (Ministry of Forestry). The original data
contained information on entire Sumatra Island area. This data then filtered by
`script.py` to only include relevant data for Singkep Island. The relevant data
node id is picked manually using GIS tool.

Source <http://appgis.dephut.go.id/appgis/kml.aspx>  
See `Lahan Kritis > Sumatera.kml`.

**License** by [Kementrian Kehutanan Republik Indonesia](http://dephut.go.id),
all right reserved.


## License

The collecting script and data presentation is licensed under MIT.  
All other data licensed by their respective provider as explained above.
