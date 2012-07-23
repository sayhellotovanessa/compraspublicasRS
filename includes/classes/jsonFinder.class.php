<?
	//ini_set('display_errors', 0);
	
	class jsonFinder {
		var $file;
		var $result = array();
		
		function __construct($file) {
				$this->file = json_decode($file);
		} 
			
		function getAll($criteria) {			
			foreach($this->file as $index) {
				if(isset($index->$criteria))
					array_push($this->result, $index->$criteria);
			}
			
			return $this->result;
		}
		
		function search($criteria, $term) {
			foreach($this->file as $index) {
				foreach($index as $field) {
					if($field == $criteria) {
						if(strstr(strtolower($index->$criteria), strtolower($term))) 
							array_push($this->result, $index);
					}
				}
			}
			return $this->result;
		}
	}
	
	/*Examples*/
	
	/*
	//FIND IN JSON WITH TERMS
	
	$devTweetstoGF = new jsonFinder('https://api.twitter.com/1/statuses/user_timeline.json?screen_name=maclovinbr&count=200');
	$tweetstomyGF = $devTweetstoGF->search('text', 'nessoila');
	
	foreach($tweetstomyGF as $tweet) {
		echo "\n$tweet->text <br/>\n";
	}
	
	*/
	
	/* 
	//OR GET ALL DATA
	
	$devTweets = new jsonFinder('https://api.twitter.com/1/statuses/user_timeline.json?screen_name=maclovinbr&count=100');
	$allDevTweets = $devTweets->getAll('text');

	foreach($allDevTweets as $devTweet) {
		echo "\n $devTweet <br/> \n" ;
	}
	*/
	
?>
