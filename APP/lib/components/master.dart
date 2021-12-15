import 'package:flutter/material.dart';
import 'package:eco_guide/components/map.dart';
import 'package:eco_guide/components/home.dart';
import 'package:eco_guide/components/announce.dart';
import 'package:eco_guide/components/ecoguide.dart';
import 'package:eco_guide/components/news.dart';


class MasterPage extends StatefulWidget {
  const MasterPage({Key? key}) : super(key: key);

  @override
  _MasterPage createState() => _MasterPage();
}

class _MasterPage extends State<MasterPage> {
  Widget customSearchBar = const Text(
    'Eco Guide',
    style: TextStyle(
        fontFamily: 'Roboto',
        fontSize: 24,
        fontWeight: FontWeight.bold
    ),
  );
  Icon customIcon = const Icon(Icons.search);

  int _selectedIndex = 0;

  static const TextStyle optionStyle =
  TextStyle(fontSize: 30, fontWeight: FontWeight.bold);

  static const List<Widget> _widgetOptions = <Widget>[
    HomePage(),
    EcoGuidePage(),
    MapPage(),
    NewsPage(),
    AnnouncePage(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: customSearchBar,
        automaticallyImplyLeading: false,
        centerTitle: true,
        actions: [
          IconButton(
              onPressed: () {
                setState(() {
                  if (customIcon.icon == Icons.search) {
                    customIcon = const Icon(Icons.cancel);
                    customSearchBar = const ListTile(
                        leading: Icon(
                          Icons.search,
                          color: Colors.white,
                          size: 28,
                        ),
                        title: TextField(
                          decoration: InputDecoration(
                            hintText: 'Введите запрос...',
                            hintStyle: TextStyle(
                              fontFamily: 'Roboto',
                              color: Colors.white,
                              fontSize: 18,
                              fontStyle: FontStyle.italic,
                            ),
                          ),
                          style: TextStyle(
                            color: Colors.white,
                          ),
                        ));
                  } else {
                    customIcon = const Icon(Icons.search);
                    customSearchBar = const Text(
                      'Eco Guide',
                      style: TextStyle(
                        fontFamily: 'Roboto',
                        fontSize: 24,
                      ),
                    );
                  }
                });
              },
              icon: customIcon)
        ],
      ),
      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: ImageIcon(
              AssetImage("assets/icons/eco-house.png"),
            ),
            label: 'Главная',
          ),
          BottomNavigationBarItem(
            icon: ImageIcon(
              AssetImage("assets/icons/eco-book.png"),
            ),
            label: 'Экогид',
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.home,
            ),
            label: 'Карта',
          ),
          BottomNavigationBarItem(
            icon: ImageIcon(
              AssetImage("assets/icons/eco-timeline.png"),
            ),
            label: 'Лента',
          ),
          BottomNavigationBarItem(
              icon: ImageIcon(
                AssetImage("assets/icons/eco-recycle.png"),
              ),
              label: 'Объявления'),
        ],
        backgroundColor: Colors.green,
        currentIndex: _selectedIndex,
        unselectedItemColor: Colors.black,
        selectedItemColor:  Colors.green,
        selectedIconTheme: IconThemeData(color: Colors.green, size: 40),
        showSelectedLabels: true,
        showUnselectedLabels: true,
        onTap: _onItemTapped,
      ),
    );
  }
}
