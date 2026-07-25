import 'package:flutter/material.dart';
import 'dart:math';
import 'dart:async';

void main() {
  runApp(MantisApp());
}

class MantisApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MANTIS Lite',
      theme: ThemeData(
        primarySwatch: Colors.orange,
        brightness: Brightness.dark,
        scaffoldBackgroundColor: Colors.black,
        fontFamily: 'Courier',
      ),
      home: MantisScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MantisScreen extends StatefulWidget {
  @override
  _MantisScreenState createState() => _MantisScreenState();
}

class _MantisScreenState extends State<MantisScreen> {
  final Random _random = Random();
  final ScrollController _scrollController = ScrollController();
  List<String> _logLines = [];
  bool _isRunning = false;
  String _currentOperation = "";
  Timer? _logTimer;
  
  final List<String> _operations = [
    "Initialize Autonomous Link",
    "Calibrate Sensor Array",
    "Sync Fleet Telemetry", 
    "Validate Safety Interlocks",
    "Run Diagnostic Sweep",
    "Optimize Signal Path",
    "Reset Mesh Topology",
    "Emergency Override"
  ];
  
  final List<String> _verbs = [
    "Calibrating", "Syncing", "Handshaking", "Negotiating", "Buffering",
    "Optimizing", "Aligning", "Polling", "Querying", "Validating",
    "Propagating", "Transcoding", "Multiplexing", "Demodulating"
  ];
  
  final List<String> _nouns = [
    "phase array", "Fresnel zone", "carrier signal", "packet stream",
    "quantum buffer", "harmonic resonance", "baseband", "sideband",
    "cryptographic nonce", "handshake token", "CRC checksum",
    "latency profile", "attenuation curve", "spectral density"
  ];
  
  final List<String> _systems = [
    "autonomous subsystem", "CAN bus bridge", "sensor fusion module",
    "telemetry aggregator", "diagnostic relay", "safety interlock"
  ];

  @override
  void initState() {
    super.initState();
    _addLogLine("MANTIS v2.8.0-FIELD initialized");
    _addLogLine("Diagnostic interface ready");
    _addLogLine("Work safe. Watch your step.");
  }

  @override
  void dispose() {
    _logTimer?.cancel();
    super.dispose();
  }

  void _addLogLine(String line) {
    setState(() {
      _logLines.add("[${DateTime.now().toString().substring(11, 19)}] $line");
      if (_logLines.length > 100) _logLines.removeAt(0);
    });
    
    // Auto-scroll to bottom
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: Duration(milliseconds: 200),
          curve: Curves.easeOut,
        );
      }
    });
  }

  String _randomGibberish() {
    final templates = [
      "${_verbs[_random.nextInt(_verbs.length)]} ${_nouns[_random.nextInt(_nouns.length)]}...",
      "${_systems[_random.nextInt(_systems.length)]} handshake established",
      "Signal strength: -${45 + _random.nextInt(40)} dBm",
      "Latency: ${2.5 + _random.nextDouble() * 42.8}ms",
      "CRC validation: 0x${_random.nextInt(0xFFFF).toRadixString(16).toUpperCase()}",
      "Channel ${1 + _random.nextInt(165)}: ${['clear', 'optimal', 'congested'][_random.nextInt(3)]}",
    ];
    return templates[_random.nextInt(templates.length)];
  }

  void _runOperation(String operation) {
    if (_isRunning) return;
    
    setState(() {
      _isRunning = true;
      _currentOperation = operation;
    });
    
    _addLogLine("Starting: $operation");
    
    int steps = 3 + _random.nextInt(5);
    int currentStep = 0;
    
    _logTimer = Timer.periodic(Duration(milliseconds: 800 + _random.nextInt(1200)), (timer) {
      if (currentStep < steps) {
        _addLogLine(_randomGibberish());
        currentStep++;
      } else {
        timer.cancel();
        _addLogLine("✓ Operation completed successfully");
        _addLogLine("All systems nominal");
        setState(() {
          _isRunning = false;
          _currentOperation = "";
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('MANTIS LITE', 
          style: TextStyle(fontWeight: FontWeight.bold, letterSpacing: 2)),
        backgroundColor: Colors.orange[800],
        centerTitle: true,
      ),
      body: Column(
        children: [
          // Header
          Container(
            width: double.infinity,
            padding: EdgeInsets.all(12),
            color: Colors.grey[900],
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text("Mining Autonomous Network Telemetry Interface",
                  style: TextStyle(color: Colors.orange, fontSize: 12, fontWeight: FontWeight.bold)),
                Text("Operator: Field Tech | Status: ${_isRunning ? 'ACTIVE' : 'READY'}",
                  style: TextStyle(color: Colors.white70, fontSize: 11)),
              ],
            ),
          ),
          
          // Log area
          Expanded(
            flex: 3,
            child: Container(
              margin: EdgeInsets.all(8),
              padding: EdgeInsets.all(12),
              decoration: BoxDecoration(
                border: Border.all(color: Colors.orange[800]!),
                borderRadius: BorderRadius.circular(4),
              ),
              child: ListView.builder(
                controller: _scrollController,
                itemCount: _logLines.length,
                itemBuilder: (context, index) {
                  return Padding(
                    padding: EdgeInsets.symmetric(vertical: 2),
                    child: Text(
                      _logLines[index],
                      style: TextStyle(
                        color: Colors.green[300],
                        fontSize: 11,
                        fontFamily: 'Courier',
                      ),
                    ),
                  );
                },
              ),
            ),
          ),
          
          // Operation buttons
          Expanded(
            flex: 2,
            child: Container(
              padding: EdgeInsets.all(8),
              child: GridView.builder(
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2,
                  crossAxisSpacing: 8,
                  mainAxisSpacing: 8,
                  childAspectRatio: 2.5,
                ),
                itemCount: _operations.length,
                itemBuilder: (context, index) {
                  return ElevatedButton(
                    onPressed: _isRunning ? null : () => _runOperation(_operations[index]),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.orange[700],
                      foregroundColor: Colors.white,
                      disabledBackgroundColor: Colors.grey[700],
                    ),
                    child: Text(
                      _operations[index],
                      style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold),
                      textAlign: TextAlign.center,
                    ),
                  );
                },
              ),
            ),
          ),
          
          // Status bar
          Container(
            width: double.infinity,
            padding: EdgeInsets.all(12),
            color: _isRunning ? Colors.orange[800] : Colors.grey[800],
            child: Text(
              _isRunning ? "Running: $_currentOperation..." : "Ready for operation",
              style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
          ),
        ],
      ),
    );
  }
}