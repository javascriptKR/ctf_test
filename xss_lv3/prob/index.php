
<html lang="en">
    <head>
        <title>XSS</title>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.9.6/tailwind.min.css">              
        <link rel="stylesheet" href="/textarea.css">
		<script src="alert.js"></script>
    </head>
    <body>
        <div class="flex items-center justify-center h-screen bg-gray-200">
            <div class="bg-white rounded-lg border shadow-lg p-4 w-1/3">
				<form method="GET">
					<label class='text-gray-800 font-regular'>Comment</label>
					<p class='text-gray-400 text-sm p-0 m-0'>alert로 document.domain을 띄우시오!</p>
					<textarea name='comment' maxlength='50' class='bg-gray-200 p-1 h-20 w-full mt-0 good'></textarea>
					<input name="param" style="margin-top: 10; width:100%; border-radius: 10px; background-color:#d6f1ff;" type="submit" value="보내기" disabled/>
					<?php
						if(isset($_GET['param'])){
							$comm = $_GET['param'];

							if($comm == 89 && $comm !== '89' && $comm !== 89 && strlen(trim($comm)) == 2)
								echo "입력한 값: ".$comm;
						}
					?>
				</form>
				<span id="msg" style></span>
            </div>
        </div>
    </body>
</html>