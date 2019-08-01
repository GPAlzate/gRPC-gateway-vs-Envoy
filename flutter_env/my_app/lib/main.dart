import 'dart:collection';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

Map<String, Company> companyData = SplayTreeMap();

class Company{
    String name;
    int openings;
    bool brokerage;
    int code;

    Company([this.code = 0, this.name = "", this.openings = 0, this.brokerage = false]);
}

void main() {
    runApp(MaterialApp(
        theme: ThemeData(
            brightness: Brightness.light,
            fontFamily: 'Montserrat',
        ),
        title: 'Companies',
        home: ListPage(),
    ));
}

class ListPage extends StatefulWidget{
    @override
    _ListPageState createState() => _ListPageState();
}

class _ListPageState extends State<ListPage>{
    Future<Map<String, Company>> _listCompanies() async{

        var data = await http.get("http://localhost:4748/companies");
        var companies = json.decode(data.body);
        var company;
        String name;

        for(var c in companies){
            company = c['company'];
            name = company['companyName'];
            companyData[name] =
                Company(
                    company['companyCode'], name,
                    company['numOpenings'], company['isBrokerage']
                );
        }
        return companyData;
    }

    void createCompany(){
        Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => CreatePage()),
        );
    }

    void _deleteCompany(String key){
        int code = companyData[key].code;
        http.delete("http://localhost:4748/delete/$code");
        companyData.remove(key);
    }

    @override
    Widget build(BuildContext context){
        return Scaffold(
            appBar: AppBar(
                title: Text('Companies'),
                backgroundColor: Colors.lightBlue[800],
                actions: <Widget>[
                    IconButton(
                        icon: Icon(
                            Icons.add,
                            color: Colors.white,
                        ),
                        onPressed: () => createCompany()
                    )
                ],
            ),
            body: Container(
                child: FutureBuilder(
                    future: _listCompanies(),
                    builder: (BuildContext context, AsyncSnapshot<Map<String, Company>> snapshot){
                        if(snapshot.data == null){
                            return Container(
                                child: Center(
                                    child: Text("Loading...")
                                ),
                            );
                        }
                        else{
                            return Container(
                                height: MediaQuery.of(context).size.height,
                                child: ListView.builder(
                                    itemCount: snapshot.data.length,
                                    itemBuilder: (BuildContext context, int i){
                                        String key = companyData.keys.elementAt(i);
                                        return Dismissible(
                                            key: Key(key),
                                            onDismissed: (dir) {
                                                setState(() {
                                                    _deleteCompany(key);
                                                });
                                                Scaffold.of(context).showSnackBar(SnackBar(content: Text("$key deleted")));
                                            },
                                            background: Container(
                                                color: Colors.red,
                                                child: Icon(Icons.delete_forever, color: Colors.white)
                                            ),
                                            child: ListTile(
                                                //TODO: onTap to see details
                                                title: Text(
                                                    key,
                                                    style: TextStyle(
                                                        fontWeight: FontWeight.bold
                                                    )
                                                ),
                                                subtitle: Text(companyData[key].code.toString()),
                                            ),
                                        );  
                                    },
                                )
                            );
                        } // else
                    }, // builder
                )
            ),
        );
    }
}

class CreatePage extends StatefulWidget{
    @override
    _CreatePageState createState() => _CreatePageState();
}

class _CreatePageState extends State<CreatePage>{

    var _company = Company();
    String brok = "Brokerage";
    final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

    void _createCompany(){

        Map<String, dynamic> request = new Map<String, dynamic>();
        request['companyName'] = "'" + _company.name.trimRight()  + "'";
        request['companyCode'] = _company.code;
        request['numOpenings'] = _company.openings;
        request['isBrokerage'] = _company.brokerage;

        http.post(
            "http://localhost:4748/register",
            body: json.encode(request)
        );

        companyData[_company.name] = _company;

    }

    @override
    Widget build(BuildContext context){
        return Scaffold(
            appBar: AppBar(
                title: Text('Create'),
                backgroundColor: Colors.lightBlue[800],
            ),
            body: Container(
                padding: const EdgeInsets.all(10.0),
                child: Builder(
                    builder: (context) => Form(
                        key: _formKey,
                        child: Column(
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            children: <Widget>[
                                SizedBox(height: 20),
                                TextFormField(
                                    decoration: const InputDecoration(
                                        icon: const Icon(Icons.business),
                                        hintText: "Enter your company name",
                                        labelText: "Company Name"
                                    ),
                                    validator: (val) => val.isEmpty ? "Please specify a name." : null,
                                    onSaved: (val) => _company.name = val,
                                ),
                                TextFormField(
                                    decoration: const InputDecoration(
                                        icon: const Icon(Icons.code),
                                        hintText: "Enter a company code (8 digits)",
                                        labelText: "Company Code"
                                    ),
                                    keyboardType: TextInputType.number,
                                    validator: (code){
                                        if(code.length != 8){
                                            return "Please enter an 8-digit code.";
                                        } 
                                        if(companyData.containsKey(int.parse(code))){
                                            return "Key already in use; please enter a different key.";
                                        }
                                        return null;
                                    },
                                    onSaved: (code) => _company.code = int.parse(code)
                                ),
                                TextFormField(
                                    decoration: const InputDecoration(
                                        icon: const Icon(Icons.assessment),
                                        hintText: "How many jobs are available?",
                                        labelText: "Number of Openings"
                                    ),
                                    keyboardType: TextInputType.number,
                                    validator: (num) => int.parse(num) < 0 ? 
                                            "Please specify a valid number of job openings, if any." : 
                                            null,
                                    onSaved: (num) => _company.openings = int.parse(num),
                                ),
                                SizedBox(height: 20),
                                DropdownButtonFormField<String>(
                                    value: brok,
                                    decoration: const InputDecoration(
                                        icon: const Icon(Icons.assignment),
                                    ),
                                    items: <DropdownMenuItem<String>>[
                                        DropdownMenuItem(
                                            child: Text("Brokerage"),
                                            value: "Brokerage",
                                        ),
                                        DropdownMenuItem(
                                            child: Text("Pay per hire"),
                                            value: "Pay per hire", 
                                        )
                                    ],
                                    onChanged: (value) {
                                        setState(() => brok = value);
                                    },
                                    validator: (value) => value.isEmpty ? "Please pick a payment scheme" : null,
                                    onSaved: (value) => _company.brokerage = (value == "Brokerage") ? true : false,
                                ),
                                Padding(
                                    padding: const EdgeInsets.all(15),
                                    child: RaisedButton(
                                        onPressed: (){
                                            if(_formKey.currentState.validate()){
                                                _formKey.currentState.save();
                                                _createCompany();

                                                showDialog(
                                                    context: context,
                                                    builder: (BuildContext context){
                                                        return AlertDialog(
                                                            title: Text("Welcome to Kalibrr!"),
                                                            content: Text("Registered " + _company.name + " successfully."),
                                                            actions: <Widget>[
                                                                new FlatButton(
                                                                    child: Text("OK"),
                                                                    onPressed: (){
                                                                        Navigator.of(context).pop();
                                                                        Navigator.pop(context);
                                                                    },
                                                                )
                                                            ],
                                                        );
                                                    }
                                                );
                                            }
                                        },
                                        child: Text("Submit")
                                    ),
                                )
                            ],
                        ),
                    )
                )
            )
        );
    }
}
