# Image Retrival

## 1. Requirements Statement

​	To understand the needs of an image search engine, I am more inclined to divide the requirements into basic requirements and additional requirements. Fundamental requirements are the most basic features of a search system, including: user input, search button, and output. These three items constitute a complete event flow, that is, the user enters the information to be retrieved, clicks the search button, and views the corresponding output. But an excellent search system does much more than that. In many cases, users cannot clearly express what they want to search for, or even have no clear search target at all. An excellent search system needs to provide users with good guidance and help users better approach their search goals. So I designed a number of additional requirements around three basic characteristics, expressed as follows:

* User Inputs
  * Clear input area, supplemented by necessary instructions and guidance
  * Preview of user input image
  * Help users limit search scope
  * Quickly and easily reset search criteria
* Search button
  * Prominent button placement
* Search Result
  * Loading animations while waiting for results
  * Preview of results
* Additional Functions
  * Well-divided functions, good and beautiful layout
  * Beautiful animation

## 2. Five-step Design

### 2.1 Formulation

​	In the Formulation stage, what we need to do is to guide users to express well, and we need to have clear guidelines for user behavior, so we need a clear input area, supplemented by necessary instructions and guidance; at the same time, we need to let users Have a more intuitive understanding of their own input, therefore, user input preview is also an indispensable function.

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005022359.png" />

​	In the image upload part I designed, the top is the function prompt, the middle is the operation prompt, and the color block is the range prompt. These three prompts constitute a good user guide. When the user clicks the color block range, the file selection window will appear. Select a file to see a preview of the file.

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005050010.png" />

As shown in the figure, after selecting a certain picture, the original color block area is replaced with the preview picture of this picture, so that the user can know more clearly whether the input he has selected is correct.

### 2.2 Initiation of Action

​	The initiation of a search action may seem simple, but it has a great impact on the user experience. First of all, the location of the search button should follow the general input habits of users, that is, to fill the search information first, and then initiate the search. Therefore, the location of the search button should be located after the input and condition selection. At the same time, we need to give the user a clear prompt, that is, whether the search action is successfully submitted, which can be expressed as loading animation and so on.

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005065756.png" />

This is the search input part I designed. You can see that from top to bottom, there are input, refinement, reset and submission, which provides users with a smooth input experience. After clicking search, a loading animation will appear to remind the user that the search is in progress, please be patient.

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005080936.png" />

### 2.3 Review of Results

​	The function of this stage is mainly reflected in the preview of the results, and the corresponding image search system is the preview of the image results. After the loading animation, you can see that the search results appear in the blank area on the right, and users can view them freely.

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005096173.png" />

### 2.4 Refinement

​	Refinement allows users to approach the desired results. Here I built a tag search system, which can also be seen in the picture above. Click on a tag, the corresponding tag will light up, and the user will It can be known that this tag has been selected. Clicking on a lit tag will turn off the tag, which is reflected in the cancellation of the selection of this tag. Users can also click on multiple tags to query multiple conditions at the same time.

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005110984.png" />

### 2.5 Use

​	After obtaining the result, the user can operate the result, which is embodied as a favorite function here, and the user can favorite the picture or cancel the favorite. Here I provide an easy to operate favorites system.

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005132510.png" />

​	As you can see, there is a button in the upper right corner of the obtained result. If you click the button, the picture will be automatically added to the favorites, and the status of the picture is Favorites.

<img src="F:\Typora\Images\image-1676005141934.png" />

​	Click the folder icon in the lower right corner to view your favorite pictures. Click the icon in the upper right corner again to cancel the favorite

<img src="https://api.aiysosis.ink/files?path=imagesOrigin/image-1676005158093.png" />