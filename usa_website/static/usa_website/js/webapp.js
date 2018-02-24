      var oldData = 2015;
      //load csvs
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/Argentina.csv' %}",
          dataType: "text",
          success: function(argentinaset){
            plot(argentinaset)
            argentina=argentinaset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/Benin.csv' %}",
          dataType: "text",
          success: function(beninset){
            benin=beninset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/china.csv' %}",
          dataType: "text",
          success: function(chinaset){
            china=chinaset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/Guatemala.csv' %}",
          dataType: "text",
          success: function(guatemalaset){
            guatemala=guatemalaset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/Nigeria.csv' %}",
          dataType: "text",
          success: function(nigeriaset){
            nigeria=nigeriaset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/Sudan.csv' %}",
          dataType: "text",
          success: function(sudanset){
            sudan=sudanset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/Tunisia.csv' %}",
          dataType: "text",
          success: function(tunisiaset){
            tunisia=tunisiaset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/unitedstates.csv' %}",
          dataType: "text",
          success: function(usset){
            us=usset;
          }
        });
      });
      $(document).ready(function() {
        $.ajax({
          type: "GET",
          url: "{% static 'usa_website/csv/world.csv' %}",
          dataType: "text",
          success: function(worldset){
            world=worldset;
          }
        });
      });
      //base functionality for clearing paths
      $(function(){
        $('#clear').on('click', function (e) {
          d3.select("svg").remove("path");
          oldData = 2015;
          var ValueUN = $('#UNans').attr('class')
          var ValueTS = $('#TSans').attr('class')
          var ValueML = $('#MLans').attr('class')
          if (ValueUN == 'new') {
            $('#UNans').removeClass("new")
            $('#UNans').addClass("orig");
          }
          if (ValueTS == 'new') {
            $('#TSans').removeClass("new")
            $('#TSans').addClass("orig");
          }
          if (ValueML == 'new') {
            $('#MLans').removeClass("new")
            $('#MLans').addClass("orig");
          }
          plot(argentina)
          });
        });
//placeholder
      //adding un-projection key for un model
      $(function(){
        $('#UNans').on('click', function (e) {
		        // Update whether or not the elements are active
            var active   = unproj.active ? false:true ,
  		        newOpacity = active ? 1 : 0;
  		          // Hide or show the elements
        console.log(newOpacity)
  		      d3.select("#unproj").attr("opacity", newOpacity);

              unproj.active = active;
              //toggle color
              var gValue = $(this).attr('class');
              if (gValue == 'orig') {
                $(this).removeClass("orig");
                $(this).addClass("new");
              } else {
                $(this).removeClass("new");
                $(this).addClass("orig");
              }
          });
        });

      $(function(){
        $('#MLans').on('click', function (e) {
  		       // Update whether or not the elements are active
           var active   = ML.active ? false:true ,
              newOpacity = active ? 1 : 0;
     	         // Hide or show the elements
           d3.select("#ML").attr("opacity", newOpacity);
      	     ML.active = active;
             //toggle color
             var gValue = $(this).attr('class');
             if (gValue == 'orig') {
               $(this).removeClass("orig");
               $(this).addClass("new");
             } else {
               $(this).removeClass("new");
               $(this).addClass("orig");
             }
          });
        });

      $(function(){
        $('#TSans').on('click', function (e) {
  		       // Update whether or not the elements are active
            var active   = TS.active ? false:true ,
    		       newOpacity = active ? 1 : 0;
    		         // Hide or show the elements
    		     d3.select("#TS").attr("opacity", newOpacity);
  		         TS.active = active;
               //toggle color
             var gValue = $(this).attr('class');
             if (gValue == 'orig') {
               $(this).removeClass("orig");
               $(this).addClass("new");
             } else {
               $(this).removeClass("new");
               $(this).addClass("orig");
             }
          });
        });
      //configuring the dropdown menu
      $("div.dropdown-content a").click(function() {
        if (this.href.includes("#argentina")) {
          oldData = 2015;
          d3.select("svg").remove();
          plot(argentina);
        //adds functionality for the clear button depending on current href
          $(function(){
            $('#clear').on('click', function (e) {
              d3.select("svg").remove("path")
              oldData = 2015
              var ValueUN = $('#UNans').attr('class')
              var ValueTS = $('#TSans').attr('class')
              var ValueML = $('#MLans').attr('class')
              if (ValueUN == 'new') {
                $('#UNans').removeClass("new")
                $('#UNans').addClass("orig");
              }
              if (ValueTS == 'new') {
                $('#TSans').removeClass("new")
                $('#TSans').addClass("orig");
              }
              if (ValueML == 'new') {
                $('#MLans').removeClass("new")
                $('#MLans').addClass("orig");
              }
              plot(argentina)
            }
        )}
      )}
         if (this.href.includes("#benin")) {
          oldData = 2015;
          d3.select("svg").remove();
          plot(benin);
          $(function(){
            $('#clear').on('click', function (e) {
              d3.select("svg").remove("path");
              oldData = 2015;
              var ValueUN = $('#UNans').attr('class')
              var ValueTS = $('#TSans').attr('class')
              var ValueML = $('#MLans').attr('class')
              if (ValueUN == 'new') {
                $('#UNans').removeClass("new")
                $('#UNans').addClass("orig");
              }
              if (ValueTS == 'new') {
                $('#TSans').removeClass("new")
                $('#TSans').addClass("orig");
              }
              if (ValueML == 'new') {
                $('#MLans').removeClass("new")
                $('#MLans').addClass("orig");
              }
              plot(benin)}
        )})
      }if (this.href.includes("#china")) {
         oldData = 2015;
         d3.select("svg").remove();
         plot(china);
         $(function(){
           $('#clear').on('click', function (e) {
             d3.select("svg").remove("path");
             oldData = 2015;
             var ValueUN = $('#UNans').attr('class')
             var ValueTS = $('#TSans').attr('class')
             var ValueML = $('#MLans').attr('class')
             if (ValueUN == 'new') {
               $('#UNans').removeClass("new")
               $('#UNans').addClass("orig");
             }
             if (ValueTS == 'new') {
               $('#TSans').removeClass("new")
               $('#TSans').addClass("orig");
             }
             if (ValueML == 'new') {
               $('#MLans').removeClass("new")
               $('#MLans').addClass("orig");
             }
             plot(china)}
       )})
       }if (this.href.includes("#guatemala")) {
          oldData = 2015;
          d3.select("svg").remove();
          plot(guatemala);
          $(function(){
            $('#clear').on('click', function (e) {
              d3.select("svg").remove("path");
              oldData = 2015;
              var ValueUN = $('#UNans').attr('class')
              var ValueTS = $('#TSans').attr('class')
              var ValueML = $('#MLans').attr('class')
              if (ValueUN == 'new') {
                $('#UNans').removeClass("new")
                $('#UNans').addClass("orig");
              }
              if (ValueTS == 'new') {
                $('#TSans').removeClass("new")
                $('#TSans').addClass("orig");
              }
              if (ValueML == 'new') {
                $('#MLans').removeClass("new")
                $('#MLans').addClass("orig");
              }
              plot(guatemala)}
        )})
        }if (this.href.includes("#nigeria")) {
          oldData = 2015;
          d3.select("svg").remove();
          plot(nigeria);
          $(function(){
            $('#clear').on('click', function (e) {
              d3.select("svg").remove("path");
              oldData = 2015;
              var ValueUN = $('#UNans').attr('class')
              var ValueTS = $('#TSans').attr('class')
              var ValueML = $('#MLans').attr('class')
              if (ValueUN == 'new') {
                $('#UNans').removeClass("new")
                $('#UNans').addClass("orig");
              }
              if (ValueTS == 'new') {
                $('#TSans').removeClass("new")
                $('#TSans').addClass("orig");
              }
              if (ValueML == 'new') {
                $('#MLans').removeClass("new")
                $('#MLans').addClass("orig");
              }
              plot(nigeria)}
        )})
        }if (this.href.includes("#sudan")) {
          oldData = 2015;
          d3.select("svg").remove();
          plot(sudan);
          $(function(){
            $('#clear').on('click', function (e) {
              d3.select("svg").remove("path");
              oldData = 2015;
              var ValueUN = $('#UNans').attr('class')
              var ValueTS = $('#TSans').attr('class')
              var ValueML = $('#MLans').attr('class')
              if (ValueUN == 'new') {
                $('#UNans').removeClass("new")
                $('#UNans').addClass("orig");
              }
              if (ValueTS == 'new') {
                $('#TSans').removeClass("new")
                $('#TSans').addClass("orig");
              }
              if (ValueML == 'new') {
                $('#MLans').removeClass("new")
                $('#MLans').addClass("orig");
              }
              plot(sudan)}
        )})
        }if (this.href.includes("#tunisia")) {
          oldData = 2015;
          d3.select("svg").remove();
          plot(tunisia);
          $(function(){
            $('#clear').on('click', function (e) {
              d3.select("svg").remove("path");
              oldData = 2015;
              var ValueUN = $('#UNans').attr('class')
              var ValueTS = $('#TSans').attr('class')
              var ValueML = $('#MLans').attr('class')
              if (ValueUN == 'new') {
                $('#UNans').removeClass("new")
                $('#UNans').addClass("orig");
              }
              if (ValueTS == 'new') {
                $('#TSans').removeClass("new")
                $('#TSans').addClass("orig");
              }
              if (ValueML == 'new') {
                $('#MLans').removeClass("new")
                $('#MLans').addClass("orig");
              }
              plot(tunisia)}
        )})
      }if (this.href.includes("#us")) {
       oldData = 2015;
       d3.select("svg").remove();
       plot(us);
       $(function(){
         $('#clear').on('click', function (e) {
           d3.select("svg").remove("path");
           oldData = 2015;
           var ValueUN = $('#UNans').attr('class')
           var ValueTS = $('#TSans').attr('class')
           var ValueML = $('#MLans').attr('class')
           if (ValueUN == 'new') {
             $('#UNans').removeClass("new")
             $('#UNans').addClass("orig");
           }
           if (ValueTS == 'new') {
             $('#TSans').removeClass("new")
             $('#TSans').addClass("orig");
           }
           if (ValueML == 'new') {
             $('#MLans').removeClass("new")
             $('#MLans').addClass("orig");
           }
           plot(us)}
     )})
   }if (this.href.includes("#world")) {
      oldData = 2015;
      d3.select("svg").remove();
      plot(world);
      $(function(){
        $('#clear').on('click', function (e) {
          d3.select("svg").remove("path");
          oldData = 2015;
          var ValueUN = $('#UNans').attr('class')
          var ValueTS = $('#TSans').attr('class')
          var ValueML = $('#MLans').attr('class')
          if (ValueUN == 'new') {
            $('#UNans').removeClass("new")
            $('#UNans').addClass("orig");
          }
          if (ValueTS == 'new') {
            $('#TSans').removeClass("new")
            $('#TSans').addClass("orig");
          }
          if (ValueML == 'new') {
            $('#MLans').removeClass("new")
            $('#MLans').addClass("orig");
          }
          plot(world)}
    )})
    }
   });

      //set margins
      var w = window.innerWidth * 0.8,
          h = window.innerHeight * 0.75,
          margin = { top: 40, right: 20, bottom: 20, left: 60 },
          radius = 4;


    function plot(data) {
      dataset = [];
      pointset =[];
      // read from CSV
      var data = d3.csv.parse(data);
      var unprojection = [];
      var timeseries_proj =[];
      var ML_proj =[];
      //splitting the datasets into their respective parts
      // += 2 is to plot every other data point
      for (var i = 1; i < 56; i += 1) {
        dataset.push({"x": parseInt(data[i].Date), "y": parseFloat(data[i].FertilityRate)});
      }

      for (var i = 1; i < 56; i += 2) {
        pointset.push({"x": parseInt(data[i].Date), "y": parseFloat(data[i].FertilityRate)});
      }
      for (var i = 55; i < 58; i += 1) {
        unprojection.push({"x": parseInt(data[i].Date), "y": parseFloat(data[i].FertilityRate)});
      }
      for (var i = 58; i < 69; i += 1) {
        timeseries_proj.push({"x": parseInt(data[i].Date), "y": parseFloat(data[i].FertilityRate)});
      }
      for (var i = 69; i < data.length; i += 1) {
        ML_proj.push({"x": parseInt(data[i].Date), "y": parseFloat(data[i].FertilityRate)});
      }
      //puts svg in div container so we can center it
      var svg = d3.select("#svgcontainer").append("svg").attr({
        width: w,
        height: h,
      });
      // setting x axis boundaries
      var xScale = d3.scale.linear()
          .domain([d3.min(dataset,function (d) {return d.x}), d3.max(dataset, function (d) { return d.x + 10; })])
          .range([margin.left, w - margin.right-40]);  // Set margins for x specific
      // setting y axis boundaries
      var yScale = d3.scale.linear()
          .domain([Math.min(0,d3.min(dataset, function(d) { return d.y; })), 1.2* Math.max(d3.max(dataset, function (d) { return d.y; }),d3.max(unprojection, function (d) { return d.y; }),d3.max(timeseries_proj, function (d) { return d.y; }),d3.max(ML_proj, function (d) { return d.y; }))])
          .range([h- margin.top, margin.bottom]);  // Set margins for y specific
      // defining X and Y Axis
      var xAxis = d3.svg.axis().scale(xScale).orient("bottom").tickFormat(d3.format("d"));
      var yAxis = d3.svg.axis().scale(yScale).orient("left");
      var circleAttrs = {
          cx: function(d) { return xScale(d.x); },
          cy: function(d) { return yScale(d.y); },
          r: radius
      };

      // Adds X-Axis as a 'g' element
      svg.append("g").attr({
        "class": "axis",
        transform: "translate(" + [0,h - 2* margin.bottom] + ")"  // Moves from top of screen to bottom
      }).call(xAxis);
      // Adds Y-Axis as a 'g' element
      svg.append("g").attr({
        "class": "axis",
        transform: "translate(" + [margin.left, 0] + ")"
      }).call(yAxis);

      //adds vertical dotted line on 2015
      var x = xScale(2015).toFixed(1);
      var y1 = yScale(Math.min(0,d3.min(dataset, function(d) { return d.y; }))).toFixed(1);
      var y2 = yScale(8.5).toFixed(1);
      svg.append("line")
          .style("stroke", "black")          // attach a line
          .attr("x1", x)                     // x position of the first end of the line
          .attr("y1", y1)                    // y position of the first end of the line
          .attr("x2", x)                     // x position of the second end of the line
          .attr("y2", y2)                    // y position of the second end of the line
          .style("stroke-dasharray", ("3, 3"));     // attach a line

      //draw lines between points
      var x = d3.scale.linear().range([0, w]);
      var y = d3.scale.linear().range([h, 0]);
      var linefunction = d3.svg.line()
          .x(function(d) { return xScale(d.x); })
          .y(function(d) { return yScale(d.y); })
          .interpolate("monotone");
      var path;
      path = svg.append("path")
          .attr("d", linefunction(dataset))
          .attr("stroke", "blue")
          .attr("stroke-width", 2)
          .attr("fill", "none");

      //updates initial circles
      svg.selectAll("circle")
          .data(pointset)
          .enter()
          .append("circle")
          .attr(circleAttrs)
          .on("mouseover", handleMouseOver)
          .on("mouseout", handleMouseOut);


          //un projection line
      svg.append("path")
          .attr("d", linefunction(unprojection))
          .attr("stroke", "red")
          .attr("stroke-width", 4)
          .attr("fill", "none")
          .attr("id", "unproj")
          .attr("opacity", 0);
      //time series projection line
      svg.append("path")
          .attr("d", linefunction(timeseries_proj))
          .attr("stroke", "green")
          .attr("stroke-width", 4)
          .attr("fill", "none")
          .attr("id", "TS")
          .attr("opacity", 0);
      //ML projection line
      svg.append("path")
          .attr("d", linefunction(ML_proj))
          .attr("stroke", "purple")
          .attr("stroke-width", 4)
          .attr("fill", "none")
          .attr("id", "ML")
          .attr("opacity", 0);

      svg.append("text")
              .attr("text-anchor", "middle")
              .attr("transform", "translate("+ (w/40) +","+(h/2)+")rotate(-90)")
              .attr("font-size", "20px")
              .attr("font-family", "sans-serif")
              .text("Percent Increase in Population Growth");
      svg.append("text")
              .attr("text-anchor", "middle")
              .attr("transform", "translate("+ (w/2) +","+(994*h/1000)+")")
              .attr("font-size", "20px")
              .attr("font-family", "sans-serif")
              .text("Year");

        // On Click, we want to add data to the array and chart. Points are added for integer year values
      svg.on("click", function() {
          var coords = d3.mouse(this);

          var newData= {
            "x": Math.round( xScale.invert(coords[0])),  // Takes the pixel number and converts to coordinate
            "y": d3.format(".2f")( yScale.invert(coords[1]))
          };
          if (newData.x % 2 == 0 && newData.x - xScale.invert(coords[0]) > 0) {
            newData.x = newData.x + 1
          } else if (newData.x % 2 == 0 && newData.x - xScale.invert(coords[0]) < 0) {
            newData.x = newData.x - 1
          }
          newData.y = parseFloat(newData.y);
          if (newData.y > 0 && newData.x > 2015 && newData.x <= 2025) {
            var x = 0;
            for (var i = 0; i < dataset.length; i += 1) {
              if (dataset[i].x == newData.x) {
                x = i;
                dataset[i] = newData;
              }
            }
            if (newData.x > oldData) {

              dataset.push(newData)  // Push data to our dataset array

              oldData = newData.x
              console.log(oldData)
              console.log(dataset);
            } else {
              temp = [];
              temp.push(dataset[0])
              for (var i = 1; i < dataset.length; i += 1) {
                if (newData.x >= dataset[i - 1].x && newData.x <= dataset[i].x) {
                  temp.push(newData);
                }
                temp.push(dataset[i])
              }


              dataset = temp;

            }
            const pointsets = dataset.filter(dataset => dataset.x%2==1);

            console.log(dataset);
            d3.selectAll("circle").remove();
            d3.selectAll("path").remove();
            d3.selectAll("g").remove();

            // define an X and Y Axis
            var xAxis = d3.svg.axis().scale(xScale).orient("bottom").tickFormat(d3.format("d"));
            var yAxis = d3.svg.axis().scale(yScale).orient("left");
            // Adds X-Axis as a 'g' element
            svg.append("g").attr({
              "class": "axis",  // Give class so we can style it
              transform: "translate(" + [0,h - 2* margin.bottom] + ")"  // Moves from top of screen to bottom
            }).call(xAxis);  // Call the xAxis function on the group
            // Adds Y-Axis as a 'g' element
            svg.append("g").attr({
              "class": "axis",
              transform: "translate(" + [margin.left, 0] + ")"
            }).call(yAxis);  // Call the yAxis function on the group
            var linefunctions = d3.svg.line()
                .x(function(d) { return xScale(d.x); })
                .y(function(d) { return yScale(d.y); })
                .interpolate("monotone");

          path = svg.append("path")
               //make the connecting line
            .attr("d", linefunctions(dataset))
            .attr("stroke", "blue")
            .attr("stroke-width", 2)
            .attr("fill", "none");
          //fixing toggle button bugs

          var showts=0;
          var showun=0;
          var showml=0;

          var ValueUN = $('#UNans').attr('class')
          var ValueTS = $('#TSans').attr('class')
          var ValueML = $('#MLans').attr('class')
          if (ValueUN == 'new') {
            showun=1;
          }
          if (ValueTS == 'new') {
            showts=1;
          }
          if (ValueML == 'new') {
            showml=1;
          }
//placeholder


          svg.append("path")
            .attr("d", linefunction(unprojection))
            .attr("stroke", "red")
            .attr("stroke-width", 4)
            .attr("fill", "none")
            .attr("id", "unproj")
            .attr("opacity",showun);


          svg.append("path")
            .attr("d", linefunction(timeseries_proj))
            .attr("stroke", "green")
            .attr("stroke-width", 4)
            .attr("fill", "none")
            .attr("id", "TS")
            .attr("opacity",showts);

          svg.append("path")
            .attr("d", linefunction(ML_proj))
            .attr("stroke", "purple")
            .attr("stroke-width", 4)
            .attr("fill", "none")
            .attr("id", "ML")
            .attr("opacity",showml);

          svg.selectAll("circle")
             // For new circle, go through the update process
            .data(pointsets)
            .enter()
            .append("circle")
            .attr(circleAttrs)  // Get attributes from circleAttrs var
            .on("mouseover", handleMouseOver)
            .on("mouseout", handleMouseOut);
          }
        })
      // Create Event Handlers for mouse
      function handleMouseOver(d, i) {  // Add interactivity
            // Use D3 to select element, change color and size
            d3.select(this).attr({
              fill: "blue",
              r: radius * 1.5
            });
            // Specify where to put label of text
            svg.append("text").attr({
               id: "t" + d.x + "-" + d.y + "-" + i,  // Create an id for text so we can select it later for removing on mouseout
                x: function() { return xScale(d.x) + 5; },
                y: function() { return yScale(d.y) - 15; }
            })
            .text(function() {
              return [d.x, d.y];  // Value of the text
            });
          }
      function handleMouseOut(d, i) {
            // Use D3 to select element, change color back to normal
            d3.select(this).attr({
              fill: "black",
              r: radius
            });
            // Select text by id and then remove. this part works for user plotted points but not dataset points right now. idk why it got buggy
            x = document.getElementById("t" + d.x + "-" + d.y + "-"+ i);
            x.remove();
          }
        }