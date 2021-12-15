import 'package:flutter/material.dart';


class EcoGuidePage extends StatefulWidget {
  const EcoGuidePage({Key? key}) : super(key: key);

  @override
  _EcoGuidePage createState() => _EcoGuidePage();
}

class _EcoGuidePage extends State<EcoGuidePage> {
  static const _iconTypes = <IconData>[
    Icons.cake,
    Icons.add_location_sharp,
    Icons.zoom_in_outlined,
    Icons.auto_awesome_motion,
    Icons.call_end_sharp,
    Icons.equalizer_rounded,
    Icons.wifi_lock,
    Icons.mail,
  ];

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        child: ListView(
          children: _iconTypes.map((icon) => Icon(icon)).toList(),
        ),
      )
    );
  }
}