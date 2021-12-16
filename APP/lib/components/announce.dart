import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:eco_guide/components/event_info.dart';
import 'package:http/http.dart' as http;

class AnnouncePage extends StatefulWidget {
  const AnnouncePage({Key? key}) : super(key: key);

  @override
  _AnnouncePage createState() => _AnnouncePage();
}

class _AnnouncePage extends State<AnnouncePage> {
  final url = 'http://194.58.122.239:8001/events/?format=json';
  var _postJson = [];

  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    fetchEvents();
  }

  void fetchEvents() async {
    final response = await http.get(Uri.parse(url));
    print(response.body);

    if (response.statusCode == 200) {
      var jsonData = json.decode(response.body) as List;

      setState(() {
        _postJson = jsonData;

      });
    }
  }


  @override
  Widget build(BuildContext context) {
    return Center(
      child: ListView.builder(
        shrinkWrap: true,
        itemCount: 20,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              leading: const CircleAvatar(
                backgroundImage: NetworkImage("https://memepedia.ru/wp-content/uploads/2018/12/kot-kashlyaet-mem.png")
              ),
              title: Text("Title $index"),
              subtitle: Text("Huy"),
              onTap: (){
                Navigator.push(context, MaterialPageRoute(builder: (context) => EventInfoPage()));
              },
            ),
          );
        }
      ),
    );
  }
}
