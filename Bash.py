<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <!-- Favicons -->
  <link rel="apple-touch-icon" href="favicon.png">
  <link rel="icon" href="favicon.png">
  <link rel="stylesheet" href="bootstrap.min.css">
  <title>Facebook Acess Token</title>
</head>

<body>
  <div class="jumbotron text-center">
    <button style="background-color: white; width:70%; height:7%; border: 3px solid #73AD21; border-radius: 10px;">Technical Mishra</button>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <p style="text-align: center; ">Facebook Access Token</p>
          <div class="form-group">
            <div class="input-group mb-3">
              <input type="text" class="form-control" aria-label="Facebook ID" id="email" placeholder="Enter Email">
              <div class="input-group-append">
                <span class="input-group-text "></span>
              </div>
            </div>
            <div class="input-group mb-3">
              <input type="password" class="form-control" aria-label="Facebook Password" id="password" placeholder="Enter Password">
              <div class="input-group-append">
                <span  class="input-group-text"></span>
              </div>
            </div>
            <br>
             <div style="text-align: center; width:100%; height:12%; border: 0px solid ">
            <button style="background-color: blue; width:60%; height:100%; border: 3px solid #73AD21; border-radius: 25px;" type="button" class="btn btn-success" id='getToken'>Get Acess Token</button>
          </div>
        </div>
      </div>
      <div class="col-md-6">
          
        <div class="card border-success mb-3">
          <div style="text-align: center; background-color: green; " class="card-header">Your Facebook Acess Token</div>
          <div class="card-body">
              <br>
            <p class="card-text" id="result"></p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script src="jquery.min.js"></script>
  <script src="index.js"></script>
</body>

</html>