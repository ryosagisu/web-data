$(document).ready(function(){


  $("#jenjang, #domain, #okupasi, #acm").on('click', '.custom-checkbox', function() {
    // GET THE INPUT
    var activeInput = $(this).children("input");

    if(activeInput.is(':checked')) {
      // DESELECT IF ALREADY CHECKED
      $(activeInput).prop("checked", false);
    } else {
      // SELECT IF NOT CHECKED
      $(activeInput).prop("checked", true);
    }

    // IF RADIO REMOVE SELECTION FROM OTHER OPTIONS
    if(activeInput.is('[type=radio]')){
      var nonActiveInput = $(this).siblings().children("input");
      $(nonActiveInput).prop("checked", false);
    }
  });

  $("#list-ok").click(function(){
    var selected = [], level;
    $("#hasilJenjang").text("Jenjang: ");
    $("#hasilDomain").text("Domain: ");

    $("#jenjang div").each(function(){
      if ($(this).find("input").prop("checked")) {
        level = $(this).find("input").attr('value');
        $("#hasilJenjang").append($(this).find("span").text())
      }
    });


    $("#domain div").each(function(){
      if ($(this).find("input").prop("checked")) {
        selected.push($(this).find("input").attr('value'));
        $("#hasilDomain").append($(this).find("span").text() + ", ");
      }
    });

    var data = {
        'domain': selected,
        'level': level,
        'req': "occupation",
        'ajax': true,
      }

    $.ajax({
      type: 'POST',
      contentType: "application/json; charset=utf-8",
      url: '/ajax',
      data: JSON.stringify(data),
      success: function(d){
        $( "#okupasi" ).html('');

        data = d['data'];
        for (var i = 0; i < data.length; i++) {
          var parts = data[i]["@id"].split('/');
          var id = parts.pop() || parts.pop();

          $( "#okupasi" ).append(
            '<div class="p-2 custom-checkbox">' +
            '<input type="checkbox" name="domain" value="' + id + '">' +
            '<span class="box">' + data[i]["http://localhost:5000/okupasi/name"][0]["@value"] + '</span>' +
            '</div>' );
        }
      }
    });
  });

  $("#cekPL").click(function(){
    var selected = [], level;
    $("#hasilOkupasi").text("Okupasi: ");

    $("#okupasi div").each(function(){
      if ($(this).find("input").prop("checked")) {
        selected.push($(this).find("input").attr('value'));
        $("#hasilOkupasi").append($(this).find("span").text() + ", ");
      }
    });

    var data = {
        'occupation': selected,
        'req': "competency",
        'ajax': true,
      }

    $.ajax({
      type: 'POST',
      contentType: "application/json; charset=utf-8",
      url: '/ajax',
      data: JSON.stringify(data),
      success: function(data){
        console.log(data);
        // $("#hasilUK").html('');
        // $("#hasilPengetahuan").html('');
        // $("#hasilSkill").html('');
        // $("#hasilSikap").html('');

        // json = $.parseJSON(data);
        // knowledge = [];
        // skill = [];
        // aspect = [];
        // Object.keys(json).forEach(function(k){
        //   $("#hasilUK").append("<li>" + k + "</li>");
        //   Object.keys(json[k]).forEach(function(l){
        //     if (l == "hasKnowledge") {
        //       Array.prototype.push.apply(knowledge, json[k][l]);
        //     }
        //   });

        //   Object.keys(json[k]).forEach(function(l){
        //     if (l == "hasSkill") {
        //       Array.prototype.push.apply(skill, json[k][l]);
        //     }
        //   });

        //   Object.keys(json[k]).forEach(function(l){
        //     if (l == "hasAspect") {
        //       Array.prototype.push.apply(aspect, json[k][l]);
        //     }
        //   });
        // });
        // // for (i = 0; i < json.Kompetensi.length; i++) {
        // //     $("#hasilUK").append("<li>" + json.Kompetensi[i] + "</li>")
        // // }
        // knowledge = unique(knowledge);
        // for (i = 0; i < knowledge.length; i++) {
        //     $("#hasilPengetahuan").append("<li>" + knowledge[i] + "</li>")
        // }

        // skill = unique(skill);
        // for (i = 0; i < skill.length; i++) {
        //     $("#hasilSkill").append("<li>" + skill[i] + "</li>")
        // }

        // aspect = unique(aspect);
        // for (i = 0; i < aspect.length; i++) {
        //     $("#hasilSikap").append("<li>" + aspect[i] + "</li>")
        // }
      }
    });
  });

  $("#listAcm").click(function(){
    var selected = [], acm = [];
    $("#hasilOkupasi").text("Okupasi: ");

    $("#okupasi div").each(function(){
      if ($(this).find("input").prop("checked")) {
        selected.push($(this).find("input").attr('value'));
        $("#hasilOkupasi").append($(this).find("span").text() + ", ");
      }
    });

    $("#acm div").each(function(){
      if ($(this).find("input").prop("checked")) {
        acm.push($(this).find("input").attr('value'));
      }
    });

    var data = {
        'occupation': selected,
        'acm': acm,
        'req': "compare",
        'ajax': true,
      }

    $.ajax({
      type: 'POST',
      contentType: "application/json; charset=utf-8",
      url: '/ajax',
      data: JSON.stringify(data),
      success: function(d){
        $( "#competencyList" ).html('');
        $( "#acmList" ).html('');

        $( "#competency" ).html('');
        competency = d['data']['competency']['element'];
        var key, i, parts, id, elements, name, dom, ordDom;
        for (key in competency) {
          parts = key.split('/');
          id = parts.pop() || parts.pop();

          elements = competency[key];
          for (i = 0; i < elements.length; i++) {
            // $( "#competency" ).append('<div><input type="text" name="' + id + '" class="competency" list="acmList"/>' + elements[i] + '</div>');
            $( "#competency" ).append('<div>' +
              '<select class="competency" id="' + id + '.' + zeroFill(i+1, 2) + '">' + 
              '<option value=""></option></select>' + 
              '<span>' + elements[i] + '</span></div>');
          }

          $('#competencyList').append($('<option>', { 
            value: id,
            text : id 
          }));
        }

        $( "#skill" ).html('');
        skill = d['data']['competency']['skill'];
        for (i = 0; i < skill.length; i++) {
          // $( "#skill" ).append('<div><input type="text" name="skill-' + i + '" class="competency" list="acmList"/>' + skill[i] + '</div>');
          $( "#skill" ).append('<div>' +
              '<select class="competency" id="Skill.' + zeroFill(i+1, 2) + '"><option value=""></option></select>' + 
              '<span>' + skill[i] + '</span></div>');
        }

        $( "#knowledge" ).html('');
        knowledge = d['data']['competency']['knowledge'];
        for (i = 0; i < knowledge.length; i++) {
          // $( "#knowledge" ).append('<div><input type="text" name="knowledge-' + i + '" class="competency" list="acmList"/>' + knowledge[i] + '</div>');
          $( "#knowledge" ).append('<div>' +
              '<select class="competency" id="Knowledge.' + zeroFill(i+1, 2) + '"><option value=""></option></select>' + 
              '<span>' + knowledge[i] + '</span></div>');
        }

        acmList = {};
        acm = d['data']['acm'];
        $( "#acmInfo" ).html('');
        for (key in acm) {
          // $( "#acmInfo" ).append('<h4 class="text-center">' + acm[key]['name'] + '</h4>');
            acmList[key] = []

          for (dom in acm[key]['hasDomains']) {
            acmList[key].push(dom);
            // for (i = 0; i < acm[key]['hasDomains'][dom].length; i++) {
            //   name = dom + '.' + i;
            //   acm[key]['hasDomains'][dom][i]
            //   $( "#acmInfo" ).append('<div>' +
            //     '<input type="text" name="' + name + '" list="competencyList" disabled/>' + 
            //     name + ': ' + acm[key]['hasDomains'][dom][i] + 
            //     '</div>');
            //   acmList.push(name);
            // }
          }
          acmList[key].sort();
        }

        for (key in acmList) {
          $( "#acmInfo" ).append('<h4 class="text-center">' + acm[key]['name'] + '</h4><br/>');

          for (i = 0; i < acmList[key].length; i++) {
            for (j = 0; j < acm[key]['hasDomains'][acmList[key][i]].length; j++) {
              name = acmList[key][i] + '.' + (j+1);
              $( "#acmInfo" ).append('<div>' +
                '<input type="text" id="' + name + '" disabled />' + 
                '<span>' + name + ': ' + acm[key]['hasDomains'][acmList[key][i]][j] + '</span>' + 
                // name + ': ' + acm[key]['hasDomains'][acmList[key][i]][j] + 
                '</div>');
  
              $('.competency').append($('<option>', { 
                value: name,
                text : name
              }));
            }
          }
        }

        var prev, curr, curr, selector, prevSelector, currSelector;
        $(".competency").on("focus click", function(e){
          prev = $(this).val();
        }).change(function(e) {
          curr = $(this).val();
          selector = $(this).attr("id");
          // console.log(e + " :"+ prev);
          if (prev != "") {
            prevSelector = $("input[id='" + prev + "']");

            // console.log(prevSelector.val().replace(selector, "").replace(/(^,)|(,$)/g, ""));
            prevSelector.val(prevSelector.val().replace(selector, "").replace(/(^,)|(,$)/g, ""));
          }

          currSelector = $("input[id='" + curr + "']");
          currSelector.val((currSelector.val() + "," + selector).replace(/(^,)|(,$)/g, ""));
        });
      }
    });
  });

  $("#listCompetency").click(function(){
    $("#competencyResult").html("");
    $("#skillResult").html("");
    $("#knowledgeResult").html("");
    $("#unassigned").html("");
    // $("#acmInfo input").each(function(){
    //   if ($(this).val() == "") {
    //     console.log($(this).attr("id"));
    //   }
    // });

    $("#competency select").each(function(){
      $( "#competencyResult" ).append('<div>' + 
        $(this).attr('id') + ": " + 
        $(this).siblings().text() + ", Reference: " + 
        $(this).val());

    });

    $("#skill select").each(function(){
      $( "#skillResult" ).append('<div>' + 
        $(this).attr('id') + ": " + 
        $(this).siblings().text() + ", Reference: " + 
        $(this).val());
    });

    $("#knowledge select").each(function(){
      $( "#knowledgeResult" ).append('<div>' + 
        $(this).attr('id') + ": " + 
        $(this).siblings().text() + ", Reference: " + 
        $(this).val());
    });

    $("#acmInfo span").each(function(){
      if ($(this).siblings().val() == "") {
        $( "#unassigned" ).append('<div>' + $(this).text() + '</div>');
      }
    });
  });
});

function unique(arr) {
    var u = {}, a = [];
    for(var i = 0, l = arr.length; i < l; ++i){
        if(!u.hasOwnProperty(arr[i])) {
            a.push(arr[i]);
            u[arr[i]] = 1;
        }
    }
    return a;
}


function zeroFill( number, width ){
  width -= number.toString().length;
  if ( width > 0 )
  {
    return new Array( width + (/\./.test( number ) ? 2 : 1) ).join( '0' ) + number;
  }
  return number + ""; // always return a string
}
