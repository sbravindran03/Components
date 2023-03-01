grid=[
    {
    "html":'''<div class="flex justify-center">
    <div class="relative inline-block mb-20">
        <!-- Dropdown toggle button -->
        <button class="relative z-10 flex items-center p-2 text-sm text-gray-600 bg-white border border-transparent rounded-md focus:border-blue-500 focus:ring-opacity-40 dark:focus:ring-opacity-40 focus:ring-blue-300 dark:focus:ring-blue-400 focus:ring dark:text-white dark:bg-gray-800 focus:outline-none">
            <span class="mx-1">Jane Doe</span>
            <svg class="w-5 h-5 mx-1" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 15.713L18.01 9.70299L16.597 8.28799L12 12.888L7.40399 8.28799L5.98999 9.70199L12 15.713Z" fill="currentColor"></path>
            </svg>
        </button>

        <!-- Dropdown menu -->
        <div class="absolute right-0 z-20 w-56 py-2 mt-2 overflow-hidden bg-white rounded-md shadow-xl dark:bg-gray-800">
            <a href="#" class="flex items-center p-3 -mt-2 text-sm text-gray-600 transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                <img class="flex-shrink-0 object-cover mx-1 rounded-full w-9 h-9" src="https://images.unsplash.com/photo-1523779917675-b6ed3a42a561?ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8d29tYW4lMjBibHVlfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=face&w=500&q=200" alt="jane avatar">
                <div class="mx-1">
                    <h1 class="text-sm font-semibold text-gray-700 dark:text-gray-200">Jane Doe</h1>
                    <p class="text-sm text-gray-500 dark:text-gray-400">janedoe@exampl.com</p>
                </div>
            </a>

            <hr class="border-gray-200 dark:border-gray-700 ">
            
            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                view profile
            </a>
            
            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                Settings
            </a>

            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                Keyboard shortcuts
            </a>

            <hr class="border-gray-200 dark:border-gray-700 ">
            
            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                Company profile
            </a>

            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                Team
            </a>

            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                Invite colleagues
            </a>

            <hr class="border-gray-200 dark:border-gray-700 ">
            
            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                Help
            </a>
            <a href="#" class="block px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white">
                Sign Out
            </a>
        </div>
    </div>
</div>''',
    "css":'''''',
    "js":''''''
    },
    {
    "html":'''<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>


<div class="flex justify-center h-screen">
    <div x-data="{ dropdownOpen: true }" class="relative my-32">
        <button @click="dropdownOpen = !dropdownOpen" class="relative z-10 block rounded-md bg-white p-2 focus:outline-none">
            <svg class="h-5 w-5 text-gray-800" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z" />
            </svg>
        </button>

        <div x-show="dropdownOpen" @click="dropdownOpen = false" class="fixed inset-0 h-full w-full z-10"></div>

        <div x-show="dropdownOpen" class="absolute right-0 mt-2 bg-white rounded-md shadow-lg overflow-hidden z-20" style="width:20rem;">
            <div class="py-2">
                <a href="#" class="flex items-center px-4 py-3 border-b hover:bg-gray-100 -mx-2">
                    <img class="h-8 w-8 rounded-full object-cover mx-1" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80" alt="avatar">
                    <p class="text-gray-600 text-sm mx-2">
                        <span class="font-bold" href="#">Sara Salah</span> replied on the <span class="font-bold text-blue-500" href="#">Upload Image</span> artical . 2m
                    </p>
                </a>
                <a href="#" class="flex items-center px-4 py-3 border-b hover:bg-gray-100 -mx-2">
                    <img class="h-8 w-8 rounded-full object-cover mx-1" src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80" alt="avatar">
                    <p class="text-gray-600 text-sm mx-2">
                        <span class="font-bold" href="#">Slick Net</span> start following you . 45m
                    </p>
                </a>
                <a href="#" class="flex items-center px-4 py-3 border-b hover:bg-gray-100 -mx-2">
                    <img class="h-8 w-8 rounded-full object-cover mx-1" src="https://images.unsplash.com/photo-1450297350677-623de575f31c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80" alt="avatar">
                    <p class="text-gray-600 text-sm mx-2">
                        <span class="font-bold" href="#">Jane Doe</span> Like Your reply on <span class="font-bold text-blue-500" href="#">Test with TDD</span> artical . 1h
                    </p>
                </a>
                <a href="#" class="flex items-center px-4 py-3 hover:bg-gray-100 -mx-2">
                    <img class="h-8 w-8 rounded-full object-cover mx-1" src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=398&q=80" alt="avatar">
                    <p class="text-gray-600 text-sm mx-2">
                        <span class="font-bold" href="#">Abigail Bennett</span> start following you . 3h
                    </p>
                </a>
            </div>
            <a href="#" class="block bg-gray-800 text-white text-center font-bold py-2">See all notifications</a>
        </div>
    </div>
</div>''',
    "css":'',
    "js":'',
    },{
    "html":'''<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
<div class="md:flex flex-col md:flex-row md:min-h-screen w-full">
  <div @click.away="open = false" class="flex flex-col w-full md:w-64 text-gray-700 bg-white dark-mode:text-gray-200 dark-mode:bg-gray-800 flex-shrink-0" x-data="{ open: false }">
    <div class="flex-shrink-0 px-8 py-4 flex flex-row items-center justify-between">
      <a href="#" class="text-lg font-semibold tracking-widest text-gray-900 uppercase rounded-lg dark-mode:text-white focus:outline-none focus:shadow-outline">Flowtrail UI</a>
      <button class="rounded-lg md:hidden rounded-lg focus:outline-none focus:shadow-outline" @click="open = !open">
        <svg fill="currentColor" viewBox="0 0 20 20" class="w-6 h-6">
          <path x-show="!open" fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z" clip-rule="evenodd"></path>
          <path x-show="open" fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
      </button>
    </div>
    <nav :class="{'block': open, 'hidden': !open}" class="flex-grow md:block px-4 pb-4 md:pb-0 md:overflow-y-auto">
      <a class="block px-4 py-2 mt-2 text-sm font-semibold text-gray-900 bg-gray-200 rounded-lg dark-mode:bg-gray-700 dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Blog</a>
      <a class="block px-4 py-2 mt-2 text-sm font-semibold text-gray-900 bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Portfolio</a>
      <a class="block px-4 py-2 mt-2 text-sm font-semibold text-gray-900 bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">About</a>
      <a class="block px-4 py-2 mt-2 text-sm font-semibold text-gray-900 bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Contact</a>
      <div @click.away="open = false" class="relative" x-data="{ open: false }">
        <button @click="open = !open" class="flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:block hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline">
          <span>Dropdown</span>
          <svg fill="currentColor" viewBox="0 0 20 20" :class="{'rotate-180': open, 'rotate-0': !open}" class="inline w-4 h-4 mt-1 ml-1 transition-transform duration-200 transform md:-mt-1"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
        </button>
        <div x-show="open" x-transition:enter="transition ease-out duration-100" x-transition:enter-start="transform opacity-0 scale-95" x-transition:enter-end="transform opacity-100 scale-100" x-transition:leave="transition ease-in duration-75" x-transition:leave-start="transform opacity-100 scale-100" x-transition:leave-end="transform opacity-0 scale-95" class="absolute right-0 w-full mt-2 origin-top-right rounded-md shadow-lg">
          <div class="px-2 py-2 bg-white rounded-md shadow dark-mode:bg-gray-800">
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Link #1</a>
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Link #2</a>
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Link #3</a>
          </div>
        </div>
      </div>
    </nav>
  </div>
</div>''',
    "css":'',
    "js":'',
    },{
      "html":'''<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>

<div class="flex justify-center h-screen">
<div class="flex items-center my-32">
  <button class="py-2 px-4 capitalize tracking-wide bg-gray-800 text-white font-medium rounded hover:bg-gray-700 focus:outline-none focus:bg-gray-700">Download</button>

  <span class="border"></span>

  <div x-data="{ dropdownOpen: true }" class="relative">
    <button @click="dropdownOpen = !dropdownOpen" class="relative z-10 block bg-gray-800 rounded p-2 hover:bg-gray-700 focus:outline-none focus:bg-gray-700">
      <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z" />
      </svg>
    </button>

    <div x-show="dropdownOpen" @click="dropdownOpen = false" class="fixed inset-0 h-full w-full z-10"></div>

    <div x-show="dropdownOpen" class="absolute right-0 mt-2 w-48 bg-white rounded-md overflow-hidden shadow-xl z-20">
      <a href="#" class="block px-4 py-2 text-sm text-gray-800 border-b hover:bg-gray-200">small <span class="text-gray-600">(640x426)</span></a>
      <a href="#" class="block px-4 py-2 text-sm text-gray-800 border-b hover:bg-gray-200">medium <span class="text-gray-600">(1920x1280)</span></a>
      <a href="#" class="block px-4 py-2 text-sm text-gray-800 border-b hover:bg-gray-200">large <span class="text-gray-600">(2400x1600)</span></a>
    </div>
  </div>
</div>
</div>''',
    "css":'',
    "js":''
            },
    {
    "html":'''<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
<div class="w-full text-gray-700 bg-white dark-mode:text-gray-200 dark-mode:bg-gray-800">
  <div x-data="{ open: false }" class="flex flex-col max-w-screen-xl px-4 mx-auto md:items-center md:justify-between md:flex-row md:px-6 lg:px-8">
    <div class="p-4 flex flex-row items-center justify-between">
      <a href="#" class="text-lg font-semibold tracking-widest text-gray-900 uppercase rounded-lg dark-mode:text-white focus:outline-none focus:shadow-outline">Flowtrail UI</a>
      <button class="md:hidden rounded-lg focus:outline-none focus:shadow-outline" @click="open = !open">
        <svg fill="currentColor" viewBox="0 0 20 20" class="w-6 h-6">
          <path x-show="!open" fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z" clip-rule="evenodd"></path>
          <path x-show="open" fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
      </button>
    </div>
    <nav :class="{'flex': open, 'hidden': !open}" class="flex-col flex-grow pb-4 md:pb-0 hidden md:flex md:justify-end md:flex-row">
      <a class="px-4 py-2 mt-2 text-sm font-semibold text-gray-900 bg-gray-200 rounded-lg dark-mode:bg-gray-700 dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Blog</a>
      <a class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Portfolio</a>
      <a class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">About</a>
      <a class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Contact</a>
      <div @click.away="open = false" class="relative" x-data="{ open: false }">
        <button @click="open = !open" class="flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline">
          <span>Dropdown</span>
          <svg fill="currentColor" viewBox="0 0 20 20" :class="{'rotate-180': open, 'rotate-0': !open}" class="inline w-4 h-4 mt-1 ml-1 transition-transform duration-200 transform md:-mt-1"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
        </button>
        <div x-show="open" x-transition:enter="transition ease-out duration-100" x-transition:enter-start="transform opacity-0 scale-95" x-transition:enter-end="transform opacity-100 scale-100" x-transition:leave="transition ease-in duration-75" x-transition:leave-start="transform opacity-100 scale-100" x-transition:leave-end="transform opacity-0 scale-95" class="absolute right-0 w-full mt-2 origin-top-right rounded-md shadow-lg md:w-48">
          <div class="px-2 py-2 bg-white rounded-md shadow dark-mode:bg-gray-800">
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Link #1</a>
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Link #2</a>
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">Link #3</a>
          </div>
        </div>
      </div>    
    </nav>
  </div>
</div>''',
    "css":'''''',
    "js":'''''',
    },
    {
    "html":''''<!-- This is an example component -->
<div class="relative inline-flex">
  <svg class="w-2 h-2 absolute top-0 right-0 m-4 pointer-events-none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 412 232"><path d="M206 171.144L42.678 7.822c-9.763-9.763-25.592-9.763-35.355 0-9.763 9.764-9.763 25.592 0 35.355l181 181c4.88 4.882 11.279 7.323 17.677 7.323s12.796-2.441 17.678-7.322l181-181c9.763-9.764 9.763-25.592 0-35.355-9.763-9.763-25.592-9.763-35.355 0L206 171.144z" fill="#648299" fill-rule="nonzero"/></svg>
  <select class="border border-gray-300 rounded-full text-gray-600 h-10 pl-5 pr-10 bg-white hover:border-gray-400 focus:outline-none appearance-none">
    <option>Choose a color</option>
    <option>Red</option>
    <option>Blue</option>
    <option>Yellow</option>
    <option>Black</option>
    <option>Orange</option>
    <option>Purple</option>
    <option>Gray</option>
    <option>White</option>
  </select>
</div>''',
    "css":'',
    "js":'',
    }



]
timeline = [
    {
    "html":'''<h3 class="text-2xl text-gray-700 font-bold mb-6 ml-3">Latest News</h3>

<ol >
  <li class="border-l-2 border-purple-600">
    <div class="md:flex flex-start">
      <div class="bg-purple-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3.5">
        <svg aria-hidden="true" focusable="false" data-prefix="fas" class="text-white w-3 h-3" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
          <path fill="currentColor" d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"></path>
        </svg>
      </div>
      <div class="block p-6 rounded-lg shadow-lg bg-gray-100 max-w-md ml-6 mb-10">
        <div class="flex justify-between mb-4">
          <a href="#!" class="font-medium text-purple-600 hover:text-purple-700 focus:text-purple-800 duration-300 transition ease-in-out text-sm">New Web Design</a>
          <a href="#!" class="font-medium text-purple-600 hover:text-purple-700 focus:text-purple-800 duration-300 transition ease-in-out text-sm">04 / 02 / 2022</a>
        </div>
        <p class="text-gray-700 mb-6">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque scelerisque diam non nisi semper, et elementum lorem ornare. Maecenas placerat facilisis mollis. Duis sagittis ligula in sodales vehicula.</p>
        <button type="button" class="inline-block px-4 py-1.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out" data-mdb-ripple="true">Preview</button>
        <button type="button" class="inline-block px-3.5 py-1 border-2 border-purple-600 text-purple-600 font-medium text-xs leading-tight uppercase rounded hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 transition duration-150 ease-in-out" data-mdb-ripple="true">See demo</button>
      </div>
    </div>
  </li>
  <li class="border-l-2 border-green-600">
    <div class="md:flex flex-start">
      <div class="bg-green-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3.5">
        <svg aria-hidden="true" focusable="false" data-prefix="fas" class="text-white w-3 h-3" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
          <path fill="currentColor" d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"></path>
        </svg>
      </div>
      <div class="block p-6 rounded-lg shadow-lg bg-gray-100 max-w-md ml-6 mb-10">
        <div class="flex justify-between mb-4">
          <a href="#!" class="font-medium text-purple-600 hover:text-purple-700 focus:text-purple-800 duration-300 transition ease-in-out text-sm">21 000 Job Seekers</a>
          <a href="#!" class="font-medium text-purple-600 hover:text-purple-700 focus:text-purple-800 duration-300 transition ease-in-out text-sm">12 / 01 / 2022</a>
        </div>
        <p class="text-gray-700 mb-6">Libero expedita explicabo eius fugiat quia aspernatur autem laudantium error architecto recusandae natus sapiente sit nam eaque, consectetur porro molestiae ipsam an deleniti.</p>
        <button type="button" class="inline-block px-4 py-1.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out" data-mdb-ripple="true">Preview</button>
        <button type="button" class="inline-block px-3.5 py-1 border-2 border-purple-600 text-purple-600 font-medium text-xs leading-tight uppercase rounded hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 transition duration-150 ease-in-out" data-mdb-ripple="true">See demo</button>
      </div>
    </div>
  </li>
  <li class="border-l-2 border-green-600">
    <div class="md:flex flex-start">
      <div class="bg-green-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3.5">
        <svg aria-hidden="true" focusable="false" data-prefix="fas" class="text-white w-3 h-3" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
          <path fill="currentColor" d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"></path>
        </svg>
      </div>
      <div class="block p-6 rounded-lg shadow-lg bg-gray-100 max-w-md ml-6 mb-10">
        <div class="flex justify-between mb-4">
          <a href="#!" class="font-medium text-purple-600 hover:text-purple-700 focus:text-purple-800 duration-300 transition ease-in-out text-sm">Awesome Employers</a>
          <a href="#!" class="font-medium text-purple-600 hover:text-purple-700 focus:text-purple-800 duration-300 transition ease-in-out text-sm">21 / 12 / 2021</a>
        </div>
        <p class="text-gray-700 mb-6">Voluptatibus temporibus esse illum eum aspernatur, fugiat suscipit natus! Eum corporis illum nihil officiis tempore. Excepturi illo natus libero sit doloremque, laborum molestias rerum pariatur quam ipsam necessitatibus incidunt, explicabo.</p>
        <button type="button" class="inline-block px-4 py-1.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out" data-mdb-ripple="true">Preview</button>
        <button type="button" class="inline-block px-3.5 py-1 border-2 border-purple-600 text-purple-600 font-medium text-xs leading-tight uppercase rounded hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0 transition duration-150 ease-in-out" data-mdb-ripple="true">See demo</button>
      </div>
    </div>
  </li>
</ol>''',
    "css":'',
    "js":'',
    },
    {
    "html":'''<!-- This is an example component -->
<div class="max-w-2xl mx-auto">


	<ol class="relative border-l border-gray-200 dark:border-gray-700">
		<li class="mb-10 ml-4">
			<div
				class="absolute w-3 h-3 bg-gray-200 rounded-full -left-1.5 border border-white dark:border-gray-900 dark:bg-gray-700">
			</div>
			<time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">February 2022</time>
			<h3 class="text-lg font-semibold text-gray-900 dark:text-white">Application UI code in Tailwind CSS</h3>
			<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">Get access to over 20+ pages
				including a dashboard layout, charts, kanban board, calendar, and pre-order E-commerce &amp; Marketing
				pages.</p>
			<a href="#"
				class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Learn
				more <svg class="w-3 h-3 ml-2" fill="currentColor" viewBox="0 0 20 20"
					xmlns="http://www.w3.org/2000/svg">
					<path fill-rule="evenodd"
						d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
						clip-rule="evenodd"></path>
				</svg></a>
		</li>
		<li class="mb-10 ml-4">
			<div
				class="absolute w-3 h-3 bg-gray-200 rounded-full -left-1.5 border border-white dark:border-gray-900 dark:bg-gray-700">
			</div>
			<time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">March 2022</time>
			<h3 class="text-lg font-semibold text-gray-900 dark:text-white">Marketing UI design in Figma</h3>
			<p class="text-base font-normal text-gray-500 dark:text-gray-400">All of the pages and components are first
				designed in Figma and we keep a parity between the two versions even as we update the project.</p>
		</li>
		<li class="ml-4">
			<div
				class="absolute w-3 h-3 bg-gray-200 rounded-full -left-1.5 border border-white dark:border-gray-900 dark:bg-gray-700">
			</div>
			<time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">April 2022</time>
			<h3 class="text-lg font-semibold text-gray-900 dark:text-white">E-Commerce UI code in Tailwind CSS</h3>
			<p class="text-base font-normal text-gray-500 dark:text-gray-400">Get started with dozens of web components
				and interactive elements built on top of Tailwind CSS.</p>
		</li>
	</ol>

	<p class="mt-5">This timeline component is part of a larger, open-source library of Tailwind CSS components. Learn more
		by going to the official <a class="text-blue-600 hover:underline"
			href="#" target="_blank">Flowbite Documentation</a>.
	</p>
</div>''',
    "css":'',
    "js":'',
    },{
    "html":'''<div class="flex-1 bg-white rounded-lg shadow-xl mt-4 p-8">
                    <h4 class="text-xl text-gray-900 font-bold">Activity log</h4>
                    <div class="relative px-4">
                        <div class="absolute h-full border border-dashed border-opacity-20 border-secondary"></div>

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">Profile informations changed.</p>
                                <p class="text-xs text-gray-500">3 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Connected with <a href="#" class="text-blue-600 font-bold">Colby Covington</a>.</p>
                                <p class="text-xs text-gray-500">15 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">Invoice <a href="#" class="text-blue-600 font-bold">#4563</a> was created.</p>
                                <p class="text-xs text-gray-500">57 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Message received from <a href="#" class="text-blue-600 font-bold">Cecilia Hendric</a>.</p>
                                <p class="text-xs text-gray-500">1 hour ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">New order received <a href="#" class="text-blue-600 font-bold">#OR9653</a>.</p>
                                <p class="text-xs text-gray-500">2 hours ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Message received from <a href="#" class="text-blue-600 font-bold">Jane Stillman</a>.</p>
                                <p class="text-xs text-gray-500">2 hours ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->
                    </div>
                </div>''',
                "css":'',
                "js":'',
    },{
                'html':'''<div class="flex-1 bg-white rounded-lg shadow-xl mt-4 p-8">
                    <h4 class="text-xl text-gray-900 font-bold">Activity log</h4>
                    <div class="relative px-4">
                        <div class="absolute h-full border border-dashed border-opacity-20 border-secondary"></div>

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">Profile informations changed.</p>
                                <p class="text-xs text-gray-500">3 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Connected with <a href="#" class="text-blue-600 font-bold">Colby Covington</a>.</p>
                                <p class="text-xs text-gray-500">15 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">Invoice <a href="#" class="text-blue-600 font-bold">#4563</a> was created.</p>
                                <p class="text-xs text-gray-500">57 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Message received from <a href="#" class="text-blue-600 font-bold">Cecilia Hendric</a>.</p>
                                <p class="text-xs text-gray-500">1 hour ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">New order received <a href="#" class="text-blue-600 font-bold">#OR9653</a>.</p>
                                <p class="text-xs text-gray-500">2 hours ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Message received from <a href="#" class="text-blue-600 font-bold">Jane Stillman</a>.</p>
                                <p class="text-xs text-gray-500">2 hours ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->
                    </div>
                </div>''',
                "css":'',
                "js":'',
                    },{
                        "html":'''<div class="h-screen flex bg-gray-900 items-center justify-center">
  <div class="grid grid-cols-12 gap-2 gap-y-4 max-w-6xl">
    
    <!-- Video 1 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/59/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">

          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/1/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>

        </div>
      </card>
    </div>

    <!-- Video 2 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/60/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">

          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/4/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>

        </div>
      </card>
    </div>

    <!-- Video 3 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/22/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">
          
          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/88/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>

        </div>
      </card>
    </div>

    <!-- Video 4 -->
    <div class="col-span-12 sm:col-span-6 md:col-span-3">
      <card class="w-full flex flex-col">
        <div class="relative">

          <!-- Image Video -->
          <a href="#">
            <img src="https://picsum.photos/seed/90/300/200" class="w-96 h-auto" />
          </a>

          <p class="absolute right-2 bottom-2 bg-gray-900 text-gray-100 text-xs px-1 py">1:15</p>
        </div>

        <div class="flex flex-row mt-2 gap-2">
          
          <!-- Profile Picture -->
          <a href="#">
            <img src="https://picsum.photos/seed/57/40/40" class="rounded-full max-h-10 max-w-10" />
          </a>

          <!-- Description -->
          <div clas="flex flex-col">
            <a href="#">
              <p class="text-gray-100 text-sm font-semibold">Learn CSS Box Model in 8 Minutes</p>
            </a>
            <a class="text-gray-400 text-xs mt-2 hover:text-gray-100" href="#"> Web Dev Simplified </a>
            <p class="text-gray-400 text-xs mt-1">241K views . 3 years ago</p>
          </div>
          
        </div>
      </card>
    </div>
  </div>
</div>''',
"css":'',
"js":'',

                    },{
"html":'''<div class="p-5 mb-4 bg-gray-50 rounded-lg border border-gray-100 dark:bg-gray-800 dark:border-gray-700">
    <time class="text-lg font-semibold text-gray-900 dark:text-white">January 23th, 2022</time>
    <ol class="mt-3 divide-y divider-gray-200 dark:divide-gray-700">
        <li>
            <a href="#" class="block items-center p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700">
                <img class="mr-3 mb-3 w-12 h-12 rounded-full sm:mb-0" src="https://via.placeholder.com/150/0000FF/" alt="Jese Leos image">
                <div class="text-gray-600 dark:text-gray-400">
                    <div class="text-base font-normal"><span class="font-medium text-gray-900 dark:text-white">Jese Leos</span> likes <span class="font-medium text-gray-900 dark:text-white">Bonnie Green's</span> post in <span class="font-medium text-gray-900 dark:text-white"> How to start with Flowbite library</span></div>
                    <div class="text-sm font-normal">"I wanted to share a webinar zeroheight."</div>
                    <span class="inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400">
                        <svg aria-hidden="true" class="mr-1 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.083 9h1.946c.089-1.546.383-2.97.837-4.118A6.004 6.004 0 004.083 9zM10 2a8 8 0 100 16 8 8 0 000-16zm0 2c-.076 0-.232.032-.465.262-.238.234-.497.623-.737 1.182-.389.907-.673 2.142-.766 3.556h3.936c-.093-1.414-.377-2.649-.766-3.556-.24-.56-.5-.948-.737-1.182C10.232 4.032 10.076 4 10 4zm3.971 5c-.089-1.546-.383-2.97-.837-4.118A6.004 6.004 0 0115.917 9h-1.946zm-2.003 2H8.032c.093 1.414.377 2.649.766 3.556.24.56.5.948.737 1.182.233.23.389.262.465.262.076 0 .232-.032.465-.262.238-.234.498-.623.737-1.182.389-.907.673-2.142.766-3.556zm1.166 4.118c.454-1.147.748-2.572.837-4.118h1.946a6.004 6.004 0 01-2.783 4.118zm-6.268 0C6.412 13.97 6.118 12.546 6.03 11H4.083a6.004 6.004 0 002.783 4.118z" clip-rule="evenodd"></path></svg>
                        Public
                    </span> 
                </div>
            </a>
        </li>
        <li>
            <a href="#" class="block items-center p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700">
                <img class="mr-3 mb-3 w-12 h-12 rounded-full sm:mb-0" src="https://via.placeholder.com/150/0000FF/" alt="Bonnie Green image">
                <div>
                    <div class="text-base font-normal text-gray-600 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Bonnie Green</span> react to <span class="font-medium text-gray-900 dark:text-white">Thomas Lean's</span> comment</div>
                    <span class="inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400">
                        <svg aria-hidden="true" class="mr-1 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26l1.514 1.515a2.003 2.003 0 012.45 2.45l1.514 1.514a4 4 0 00-5.478-5.478z" clip-rule="evenodd"></path><path d="M12.454 16.697L9.75 13.992a4 4 0 01-3.742-3.741L2.335 6.578A9.98 9.98 0 00.458 10c1.274 4.057 5.065 7 9.542 7 .847 0 1.669-.105 2.454-.303z"></path></svg>
                        Private
                    </span> 
                </div>
            </a>
        </li>
    </ol>
</div>
<div class="p-5 bg-gray-50 rounded-lg border border-gray-100 dark:bg-gray-800 dark:border-gray-700">
    <time class="text-lg font-semibold text-gray-900 dark:text-white">January 10th, 2022</time>
    <ol class="mt-3 divide-y divider-gray-200 dark:divide-gray-700">
        <li>
            <a href="#" class="block items-center p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700">
                <img class="mr-3 mb-3 w-12 h-12 rounded-full sm:mb-0" src="https://via.placeholder.com/150/0000FF/" alt="Laura Romeros image">
                <div class="text-gray-600 dark:text-gray-400">
                    <div class="text-base font-normal"><span class="font-medium text-gray-900 dark:text-white">Laura Romeros</span> likes <span class="font-medium text-gray-900 dark:text-white">Bonnie Green's</span> post in <span class="font-medium text-gray-900 dark:text-white"> How to start with Flowbite library</span></div>
                    <div class="text-sm font-normal">"I wanted to share a webinar zeroheight."</div>
                    <span class="inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400">
                        <svg aria-hidden="true" class="mr-1 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26l1.514 1.515a2.003 2.003 0 012.45 2.45l1.514 1.514a4 4 0 00-5.478-5.478z" clip-rule="evenodd"></path><path d="M12.454 16.697L9.75 13.992a4 4 0 01-3.742-3.741L2.335 6.578A9.98 9.98 0 00.458 10c1.274 4.057 5.065 7 9.542 7 .847 0 1.669-.105 2.454-.303z"></path></svg>
                        Private
                    </span> 
                </div>
            </a>
        </li>
        <li>
            <a href="#" class="block items-center p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700">
                <img class="mr-3 mb-3 w-12 h-12 rounded-full sm:mb-0" src="https://via.placeholder.com/150/0000FF/" alt="Mike Willi image">
                <div>
                    <div class="text-base font-normal text-gray-600 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Mike Willi</span> react to <span class="font-medium text-gray-900 dark:text-white">Thomas Lean's</span> comment</div>
                    <span class="inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400">
                        <svg aria-hidden="true" class="mr-1 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.083 9h1.946c.089-1.546.383-2.97.837-4.118A6.004 6.004 0 004.083 9zM10 2a8 8 0 100 16 8 8 0 000-16zm0 2c-.076 0-.232.032-.465.262-.238.234-.497.623-.737 1.182-.389.907-.673 2.142-.766 3.556h3.936c-.093-1.414-.377-2.649-.766-3.556-.24-.56-.5-.948-.737-1.182C10.232 4.032 10.076 4 10 4zm3.971 5c-.089-1.546-.383-2.97-.837-4.118A6.004 6.004 0 0115.917 9h-1.946zm-2.003 2H8.032c.093 1.414.377 2.649.766 3.556.24.56.5.948.737 1.182.233.23.389.262.465.262.076 0 .232-.032.465-.262.238-.234.498-.623.737-1.182.389-.907.673-2.142.766-3.556zm1.166 4.118c.454-1.147.748-2.572.837-4.118h1.946a6.004 6.004 0 01-2.783 4.118zm-6.268 0C6.412 13.97 6.118 12.546 6.03 11H4.083a6.004 6.004 0 002.783 4.118z" clip-rule="evenodd"></path></svg>
                        Public
                    </span> 
                </div>
            </a>
        </li>
        <li>
            <a href="#" class="block items-center p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700">
                <img class="mr-3 mb-3 w-12 h-12 rounded-full sm:mb-0" src="https://via.placeholder.com/150/0000FF/" alt="Jese Leos image">
                <div class="text-gray-600 dark:text-gray-400">
                    <div class="text-base font-normal"><span class="font-medium text-gray-900 dark:text-white">Jese Leos</span> likes <span class="font-medium text-gray-900 dark:text-white">Bonnie Green's</span> post in <span class="font-medium text-gray-900 dark:text-white"> How to start with Flowbite library</span></div>
                    <div class="text-sm font-normal">"I wanted to share a webinar zeroheight."</div>
                    <span class="inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400">
                        <svg aria-hidden="true" class="mr-1 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.083 9h1.946c.089-1.546.383-2.97.837-4.118A6.004 6.004 0 004.083 9zM10 2a8 8 0 100 16 8 8 0 000-16zm0 2c-.076 0-.232.032-.465.262-.238.234-.497.623-.737 1.182-.389.907-.673 2.142-.766 3.556h3.936c-.093-1.414-.377-2.649-.766-3.556-.24-.56-.5-.948-.737-1.182C10.232 4.032 10.076 4 10 4zm3.971 5c-.089-1.546-.383-2.97-.837-4.118A6.004 6.004 0 0115.917 9h-1.946zm-2.003 2H8.032c.093 1.414.377 2.649.766 3.556.24.56.5.948.737 1.182.233.23.389.262.465.262.076 0 .232-.032.465-.262.238-.234.498-.623.737-1.182.389-.907.673-2.142.766-3.556zm1.166 4.118c.454-1.147.748-2.572.837-4.118h1.946a6.004 6.004 0 01-2.783 4.118zm-6.268 0C6.412 13.97 6.118 12.546 6.03 11H4.083a6.004 6.004 0 002.783 4.118z" clip-rule="evenodd"></path></svg>
                        Public
                    </span> 
                </div>
            </a>
        </li>
        <li>
            <a href="#" class="block items-center p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700">
                <img class="mr-3 mb-3 w-12 h-12 rounded-full sm:mb-0" src="https://via.placeholder.com/150/0000FF/" alt="Bonnie Green image">
                <div class="text-gray-600 dark:text-gray-400">
                    <div class="text-base font-normal"><span class="font-medium text-gray-900 dark:text-white">Bonnie Green</span> likes <span class="font-medium text-gray-900 dark:text-white">Bonnie Green's</span> post in <span class="font-medium text-gray-900 dark:text-white"> Top figma designs</span></div>
                    <div class="text-sm font-normal">"I wanted to share a webinar zeroheight."</div>
                    <span class="inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400">
                        <svg aria-hidden="true" class="mr-1 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26l1.514 1.515a2.003 2.003 0 012.45 2.45l1.514 1.514a4 4 0 00-5.478-5.478z" clip-rule="evenodd"></path><path d="M12.454 16.697L9.75 13.992a4 4 0 01-3.742-3.741L2.335 6.578A9.98 9.98 0 00.458 10c1.274 4.057 5.065 7 9.542 7 .847 0 1.669-.105 2.454-.303z"></path></svg>
                        Private
                    </span> 
                </div>
            </a>
        </li>
    </ol>
</div>''',
"css":'',
"js":'',
"html":'''<div class="container bg-gray-200 mx-auto w-full h-full">
  <div class="relative wrap overflow-hidden p-10 h-full">
    <div class="border-2-2 absolute border-opacity-20 border-gray-700 h-full border" style="left: 50%"></div>
    <!-- right timeline -->
    <div class="mb-8 flex justify-between items-center w-full right-timeline">
      <div class="order-1 w-5/12"></div>
      <div class="z-20 flex items-center order-1 bg-gray-800 shadow-Axl w-8 h-8 rounded-full">
        <h1 class="mx-auto font-semibold text-lg text-white">1</h1>
      </div>
      <div class="order-1 bg-gray-400 rounded-lg shadow-xl w-5/12 px-6 py-4">
        <h3 class="mb-3 font-bold text-gray-800 text-xl">Lorem Ipsum</h3>
        <p class="text-sm leading-snug tracking-wide text-gray-900 text-opacity-100">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
      </div>
    </div>

    <!-- left timeline -->
    <div class="mb-8 flex justify-between flex-row-reverse items-center w-full left-timeline">
      <div class="order-1 w-5/12"></div>
      <div class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-8 h-8 rounded-full">
        <h1 class="mx-auto text-white font-semibold text-lg">2</h1>
      </div>
      <div class="order-1 bg-red-400 rounded-lg shadow-xl w-5/12 px-6 py-4">
        <h3 class="mb-3 font-bold text-white text-xl">Lorem Ipsum</h3>
        <p class="text-sm font-medium leading-snug tracking-wide text-white text-opacity-100">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
      </div>
    </div>
    
    <!-- right timeline -->
    <div class="mb-8 flex justify-between items-center w-full right-timeline">
      <div class="order-1 w-5/12"></div>
      <div class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-8 h-8 rounded-full">
        <h1 class="mx-auto font-semibold text-lg text-white">3</h1>
      </div>
      <div class="order-1 bg-gray-400 rounded-lg shadow-xl w-5/12 px-6 py-4">
        <h3 class="mb-3 font-bold text-gray-800 text-xl">Lorem Ipsum</h3>
        <p class="text-sm leading-snug tracking-wide text-gray-900 text-opacity-100">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
      </div>
    </div>

    <!-- left timeline -->
    <div class="mb-8 flex justify-between flex-row-reverse items-center w-full left-timeline">
      <div class="order-1 w-5/12"></div>
      <div class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-8 h-8 rounded-full">
        <h1 class="mx-auto text-white font-semibold text-lg">4</h1>
      </div>
      <div class="order-1 bg-red-400 rounded-lg shadow-xl w-5/12 px-6 py-4">
        <h3 class="mb-3 font-bold text-white text-xl">Lorem Ipsum</h3>
        <p class="text-sm font-medium leading-snug tracking-wide text-white text-opacity-100">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
      </div>
    </div>
  </div>
</div>''',
"css":'',
"js":'',

                    }
]
typography=[
    {
    "html":'''<div class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible">
<p class="block font-sans text-sm font-light leading-normal text-inherit antialiased">Material Tailwind is an easy to use components library for Tailwind CSS and Material Design. It provides a simple way to customize your components, you can change the colors, fonts, breakpoints and everything you need.</p><div class="w-full md:w-7/12 pt-5 px-4 mb-8 mx-auto text-center">
            <div class="text-sm text-gray-700 py-1">
            This components requires
            <a
                href="https://www.material-tailwind.com?ref=tailwindcomponents"
                class="text-gray-700 font-semibold"
                target="_blank"
                >Material Tailwind CSS & JS</a
            >
            for the classes. <br /><br />
            A component by<a
                href="https://www.creative-tim.com?ref=tailwindcomponents"
                class="text-gray-700 font-semibold"
                target="_blank"
            >
                Creative Tim</a
            >.
            </div>
        </div>
      </div>''',
      "css":'',
      "js":'',
    },{
    "html":'''<div class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible">
<div class="flex flex-col gap-8 text-left"><h1 class="block font-sans text-5xl font-semibold leading-tight tracking-normal text-blue-gray-900 antialiased">Material Tailwind</h1><h1 class="block font-sans text-5xl font-semibold leading-tight tracking-normal text-blue-500 antialiased">Material Tailwind</h1><h1 class="block font-sans text-5xl font-semibold leading-tight tracking-normal text-red-500 antialiased">Material Tailwind</h1><h1 class="block font-sans text-5xl font-semibold leading-tight tracking-normal text-green-500 antialiased">Material Tailwind</h1></div><div class="w-full md:w-7/12 pt-5 px-4 mb-8 mx-auto text-center">
            <div class="text-sm text-gray-700 py-1">
            This components requires
            <a
                href="https://www.material-tailwind.com?ref=tailwindcomponents"
                class="text-gray-700 font-semibold"
                target="_blank"
                >Material Tailwind CSS & JS</a
            >
            for the classes. <br /><br />
            A component by<a
                href="https://www.creative-tim.com?ref=tailwindcomponents"
                class="text-gray-700 font-semibold"
                target="_blank"
            >
                Creative Tim</a
            >.
            </div>
        </div>
      </div>''',
      "css":'',
      "js":'',
   },{
    "html":'''<div class="flex min-h-screen items-center justify-center bg-black font-bold text-white">
  <div class=" text-center space-y-12">
      <div class="text-center text-5xl font-bold">
        Services offered
        <div class="relative inline-grid grid-cols-1 grid-rows-1 gap-12 overflow-hidden">
        <span class="animate-word col-span-full row-span-full">Flutter</span>
        <span class="animate-word-delay-1 col-span-full row-span-full">Django</span>
        <span class="animate-word-delay-2 col-span-full row-span-full">Website</span>
        <span class="animate-word-delay-3 col-span-full row-span-full">VueJS</span>
        <span class="animate-word-delay-4 col-span-full row-span-full">NuxtJS</span>
        </div>
    </div>
    <p class=" text-white">
        Want to hire me for work ping me <a class="underline" href="mailto:ponnamkarthik3@gmail.com">mail here</a>
    </p>
  </div>
</div>

<style>

@keyframes word {
  0% {
    transform: translateY(100%);
  }
  15% {
    transform: translateY(-10%);
    animation-timing-function: ease-out;
  }

  20% {
    transform: translateY(0);
  }

  40%,
  100% {
    transform: translateY(-110%);
  }
}

.animate-word {
  animation: word 7s infinite;
}
.animate-word-delay-1 {
  animation: word 7s infinite;
  animation-delay: -1.4s;
}
.animate-word-delay-2 {
  animation: word 7s infinite;
  animation-delay: -2.8s;
}
.animate-word-delay-3 {
  animation: word 7s infinite;
  animation-delay: -4.2s;
}
.animate-word-delay-4 {
  animation: word 7s infinite;
  animation-delay: -5.6s;
}

</style>''',
    "css":'',
    "js":'',
    },{
    "html":'''<div class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible">
<div class="flex flex-col gap-8 text-left"><h1 class="block font-sans text-5xl font-semibold leading-tight tracking-normal text-inherit antialiased">Material Tailwind</h1><h2 class="block font-sans text-4xl font-semibold leading-[1.3] tracking-normal text-inherit antialiased">Material Tailwind</h2><h3 class="block font-sans text-3xl font-semibold leading-snug tracking-normal text-inherit antialiased">Material Tailwind</h3><h4 class="block font-sans text-2xl font-semibold leading-snug tracking-normal text-inherit antialiased">Material Tailwind</h4><h5 class="block font-sans text-xl font-semibold leading-snug tracking-normal text-inherit antialiased">Material Tailwind</h5><p class="block font-sans text-base font-semibold capitalize leading-relaxed tracking-normal text-inherit antialiased">Material Tailwind</p></div><div class="w-full md:w-7/12 pt-5 px-4 mb-8 mx-auto text-center">
            <div class="text-sm text-gray-700 py-1">
            This components requires
            <a
                href="https://www.material-tailwind.com?ref=tailwindcomponents"
                class="text-gray-700 font-semibold"
                target="_blank"
                >Material Tailwind CSS & JS</a
            >
            for the classes. <br /><br />
            A component by<a
                href="https://www.creative-tim.com?ref=tailwindcomponents"
                class="text-gray-700 font-semibold"
                target="_blank"
            >
                Creative Tim</a
            >.
            </div>
        </div>
      </div>'''
    }
]
progress=[{
    "html":''''<script defer src="https://unpkg.com/alpinejs@3.2.4/dist/cdn.min.js"></script>    
    
<main class="grid w-full min-h-screen text-gray-100 bg-gray-900 place-content-center">

    <section x-data="skillDisplay"
        class="p-6 space-y-6 bg-gray-800 rounded-xl md:grid md:grid-cols-2 md:gap-4 sm:space-y-0">
        <div class="grid grid-cols-2 gap-6">
            <template x-for="skill in skills">
                <button x-text="skill.title"
                    class="px-4 py-2 text-xl text-gray-100 transition bg-blue-600 rounded-md h-14 w-44 hover:bg-blue-700"
                    :class="(currentSkill.title == skill.title) && 'font-bold ring-2 ring-gray-100'"
                    @click="currentSkill = skill"></button>
            </template>
        </div>

        <div class="flex items-center justify-center" x-data="{ circumference: 2 * 22 / 7 * 120 }">
            <svg class="transform -rotate-90 w-72 h-72">
                <circle cx="145" cy="145" r="120" stroke="currentColor" stroke-width="30" fill="transparent"
                    class="text-gray-700" />

                <circle cx="145" cy="145" r="120" stroke="currentColor" stroke-width="30" fill="transparent"
                    :stroke-dasharray="circumference"
                    :stroke-dashoffset="circumference - currentSkill.percent / 100 * circumference"
                    class="text-blue-500 " />
            </svg>
            <span class="absolute text-5xl" x-text="`${currentSkill.percent}%`"></span>
    </section>
</main>

<script>
    document.addEventListener('alpine:init', () => {
        Alpine.data('skillDisplay', () => ({
            skills: [{
                    'title': 'HTML',
                    'percent': '95',
                },
                {
                    'title': 'CSS',
                    'percent': '70',
                },
                {
                    'title': 'Tailwind CSS',
                    'percent': '90',
                },
                {
                    'title': 'JavaScript',
                    'percent': '70',
                },
                {
                    'title': 'Alpine JS',
                    'percent': '80',
                }, {
                    'title': 'PHP',
                    'percent': '65',
                }, {
                    'title': 'Laravel',
                    'percent': '75',
                }
            ],
            currentSkill: {
                'title': 'HTML',
                'percent': '95',
            }
        }));
    });
</script>'''
    },{
    "html":'''<div class="relative pt-1 mx-5">
  <div class="overflow-hidden h-4 mb-4 text-xs flex rounded bg-emerald-200">
    <div style="width: 10%" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-red-500"></div>
    <div style="width: 15%" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-orange-500"></div>
    <div style="width: 25%" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-emerald-500"></div>
  </div>
</div>'''
  },{
    "html":'''<script src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.2.2/cdn.js" defer></script>

<style>
    .container {
        height: 400vh;
    }
</style>

<div class="container">
    <!-- Top bar -->
    <div x-data="scrollProgress" class="fixed inset-x-0 top-0 z-50">
        <div class="h-1 bg-blue-500" :style="`width: ${percent}%`"></div>
    </div>

    <main class="w-scrren min-h-screen flex items-center justify-center">
      <h1 class="text-3xl font-medium">Scroll down</h1>
    </main>

    <!-- Circle -->
    <div
      x-data="scrollProgress"
      class="fixed inline-flex items-center justify-center overflow-hidden rounded-full bottom-5 left-5"
    >
      <!-- Building a Progress Ring: https://css-tricks.com/building-progress-ring-quickly/ -->
      <svg class="w-20 h-20">
        <circle
          class="text-gray-300"
          stroke-width="5"
          stroke="currentColor"
          fill="transparent"
          r="30"
          cx="40"
          cy="40"
        />
        <circle
          class="text-blue-600"
          stroke-width="5"
          :stroke-dasharray="circumference"
          :stroke-dashoffset="circumference - percent / 100 * circumference"
          stroke-linecap="round"
          stroke="currentColor"
          fill="transparent"
          r="30"
          cx="40"
          cy="40"
        />
      </svg>
      <span class="absolute text-xl text-blue-700" x-text="`${percent}%`"></span>
    </div>

    <!-- Social links -->
    <div class="fixed flex flex-col items-center space-y-4 bottom-5 right-5">
      <a href="https://twitter.com/ak_kamona" target="_blank" class="transition-transform transform hover:scale-125">
        <span class="sr-only">Twitter</span>
        <svg
          aria-hidden="true"
          class="w-8 h-8 text-blue-500"
          fill="currentColor"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
        >
          <path
            d="M19.633,7.997c0.013,0.175,0.013,0.349,0.013,0.523c0,5.325-4.053,11.461-11.46,11.461c-2.282,0-4.402-0.661-6.186-1.809 c0.324,0.037,0.636,0.05,0.973,0.05c1.883,0,3.616-0.636,5.001-1.721c-1.771-0.037-3.255-1.197-3.767-2.793 c0.249,0.037,0.499,0.062,0.761,0.062c0.361,0,0.724-0.05,1.061-0.137c-1.847-0.374-3.23-1.995-3.23-3.953v-0.05 c0.537,0.299,1.16,0.486,1.82,0.511C3.534,9.419,2.823,8.184,2.823,6.787c0-0.748,0.199-1.434,0.548-2.032 c1.983,2.443,4.964,4.04,8.306,4.215c-0.062-0.3-0.1-0.611-0.1-0.923c0-2.22,1.796-4.028,4.028-4.028 c1.16,0,2.207,0.486,2.943,1.272c0.91-0.175,1.782-0.512,2.556-0.973c-0.299,0.935-0.936,1.721-1.771,2.22 c0.811-0.088,1.597-0.312,2.319-0.624C21.104,6.712,20.419,7.423,19.633,7.997z"
          ></path>
        </svg>
      </a>
      <a href="https://github.com/Kamona-WD" target="_blank" class="transition-transform transform hover:scale-125">
        <span class="sr-only">Github</span>
        <svg
          aria-hidden="true"
          class="w-8 h-8 text-black"
          fill="currentColor"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
        >
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M12.026,2c-5.509,0-9.974,4.465-9.974,9.974c0,4.406,2.857,8.145,6.821,9.465 c0.499,0.09,0.679-0.217,0.679-0.481c0-0.237-0.008-0.865-0.011-1.696c-2.775,0.602-3.361-1.338-3.361-1.338 c-0.452-1.152-1.107-1.459-1.107-1.459c-0.905-0.619,0.069-0.605,0.069-0.605c1.002,0.07,1.527,1.028,1.527,1.028 c0.89,1.524,2.336,1.084,2.902,0.829c0.091-0.645,0.351-1.085,0.635-1.334c-2.214-0.251-4.542-1.107-4.542-4.93 c0-1.087,0.389-1.979,1.024-2.675c-0.101-0.253-0.446-1.268,0.099-2.64c0,0,0.837-0.269,2.742,1.021 c0.798-0.221,1.649-0.332,2.496-0.336c0.849,0.004,1.701,0.115,2.496,0.336c1.906-1.291,2.742-1.021,2.742-1.021 c0.545,1.372,0.203,2.387,0.099,2.64c0.64,0.696,1.024,1.587,1.024,2.675c0,3.833-2.33,4.675-4.552,4.922 c0.355,0.308,0.675,0.916,0.675,1.846c0,1.334-0.012,2.41-0.012,2.737c0,0.267,0.178,0.577,0.687,0.479 C19.146,20.115,22,16.379,22,11.974C22,6.465,17.535,2,12.026,2z"
          ></path>
        </svg>
      </a>
    </div>
</div>

<script>
    const scrollProgress = () => {
        return {
            init() {
                window.addEventListener('scroll', () => {
                    let winScroll = document.body.scrollTop || document.documentElement.scrollTop
                    let height = document.documentElement.scrollHeight - document.documentElement.clientHeight
                    this.percent = Math.round((winScroll / height) * 100)
                })
            },
            circumference: 30 * 2 * Math.PI,
            percent: 0,
        }
    }
</script>'''
  },{
    "html":'''<div class='loading h-1 w-[0%] bg-red-500 transition-all duration-200 absolute z-40 top-0 '></div>


<script>
	const loading = document.querySelector('.loading');
    let currentProgress = 0; 
    let itv = setInterval(function(){
        if(currentProgress < 100){
            const increment = Math.random()*40;
            currentProgress += increment;
            if(currentProgress > 100) currentProgress = 100;
            setProgress(currentProgress);
        }else{
            clearInterval(itv);
        }
    },800);

    function setProgress(progress){
        loading.style.width = `${progress}%`;
    }
    
</script>'''
  },{
    "html":'''<div class="flex min-h-screen w-full items-center justify-center bg-[#131730] px-4">
  <div class="flex w-[500px] max-w-3xl flex-col rounded bg-[#1b2042] py-12 px-6 text-slate-200">
    <h2 class="mb-2 font-serif text-2xl">Build your page</h2>
    <p class="mb-12">
      Complete actions to unlock new features along the way.<br />
      On average, completed pages get 30% more traffic.
    </p>
    <div class="mb-2 flex gap-2">
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-blue-600"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-blue-500"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-blue-400"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-blue-300"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-blue-200"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-green-200"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-gray-900"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-gray-900"></span>
      <span class="mb-2 h-[15px] flex-1 rounded-xl bg-gray-900"></span>
    </div>
    <small>3 remaining to complete</small>
  </div>
</div>'''
  }
]
Pagination =[
    {
    "html":'''<ul class="flex space-x-2 justify-center my-10 pagination-Container">
          <a href="#" class="group">
            <li class="active w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-green-700 group-hover:bg-green-700">
              <span class="text-green-700 font-medium group-hover:text-slate-200">1</span>
            </li>
          </a>

          <a href="#" class="group">
            <li class="w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-red-700 group-hover:bg-red-700">
              <span class="text-red-700 font-medium group-hover:text-slate-200">2</span>
            </li>
          </a>
          <a href="#" class="group">
            <li class="w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-orange-700 group-hover:bg-orange-700">
              <span class="text-orange-700 font-medium group-hover:text-slate-200">3</span>
            </li>
          </a>

          <a href="#" class="group">
            <li class="w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-sky-700 group-hover:bg-sky-700">
              <span class="text-sky-700 font-medium group-hover:text-slate-200">4</span>
            </li>
          </a>
        </ul>


        <ul class="flex space-x-2 justify-center my-10 pagination-Container">
          <a href="#" class="group">
            <li class="active w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-green-700 bg-green-700">
              <span class="font-medium text-slate-200">1</span>
            </li>
          </a>

          <a href="#" class="group">
            <li class="w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-red-700 bg-red-700">
              <span class="font-medium text-slate-200">2</span>
            </li>
          </a>
          <a href="#" class="group">
            <li class="w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-orange-700 bg-orange-700">
              <span class="font-medium text-slate-200">3</span>
            </li>
          </a>

          <a href="#" class="group">
            <li class="w-10 h-10 text-gray-800 grid place-items-center rounded-md border lg:border-2 border-sky-700 bg-sky-700">
              <span class="font-medium text-slate-200">4</span>
            </li>
          </a>
        </ul>'''
    },{
    "html":'''<div class="
   inline-flex
   border border-[#e4e4e4]
   bg-white
   p-4
   rounded-xl
   ">
   <ul class="flex items-center -mx-[6px]">
      <li class="px-[6px]">
         <a href="javascript:void(0)" class="
            w-9
            h-9
            flex
            items-center
            justify-center
            rounded-md
            border border-[#EDEFF1]
            text-[#838995] text-base
            hover:bg-primary hover:border-primary hover:text-white
            ">
            <span>
               <svg width="8" height="15" viewBox="0 0 8 15" class="fill-current stroke-current">
                  <path d="M7.12979 1.91389L7.1299 1.914L7.1344 1.90875C7.31476 1.69833 7.31528 1.36878 7.1047 1.15819C7.01062 1.06412 6.86296 1.00488 6.73613 1.00488C6.57736 1.00488 6.4537 1.07206 6.34569 1.18007L6.34564 1.18001L6.34229 1.18358L0.830207 7.06752C0.830152 7.06757 0.830098 7.06763 0.830043 7.06769C0.402311 7.52078 0.406126 8.26524 0.827473 8.73615L0.827439 8.73618L0.829982 8.73889L6.34248 14.6014L6.34243 14.6014L6.34569 14.6047C6.546 14.805 6.88221 14.8491 7.1047 14.6266C7.30447 14.4268 7.34883 14.0918 7.12833 13.8693L1.62078 8.01209C1.55579 7.93114 1.56859 7.82519 1.61408 7.7797L1.61413 7.77975L1.61729 7.77639L7.12979 1.91389Z" stroke-width="0.3"></path>
               </svg>
            </span>
         </a>
      </li>
      <li class="px-[6px]">
         <a href="javascript:void(0)" class="
            w-9
            h-9
            flex
            items-center
            justify-center
            rounded-md
            border border-[#EDEFF1]
            text-[#838995] text-base
            hover:bg-primary hover:border-primary hover:text-white
            ">
         1
         </a>
      </li>
      <li class="px-[6px]">
         <a href="javascript:void(0)" class="
            w-9
            h-9
            flex
            items-center
            justify-center
            rounded-md
            border border-[#EDEFF1]
            text-[#838995] text-base
            hover:bg-primary hover:border-primary hover:text-white
            ">
         2
         </a>
      </li>
      <li class="px-[6px]">
         <a href="javascript:void(0)" class="
            w-9
            h-9
            flex
            items-center
            justify-center
            rounded-md
            border border-[#EDEFF1]
            text-[#838995] text-base
            hover:bg-primary hover:border-primary hover:text-white
            ">
         3
         </a>
      </li>
      <li class="px-[6px]">
         <a href="javascript:void(0)" class="
            w-9
            h-9
            flex
            items-center
            justify-center
            rounded-md
            border border-[#EDEFF1]
            text-[#838995] text-base
            hover:bg-primary hover:border-primary hover:text-white
            ">
         4
         </a>
      </li>
      <li class="px-[6px]">
         <a href="javascript:void(0)" class="
            w-9
            h-9
            flex
            items-center
            justify-center
            rounded-md
            border border-[#EDEFF1]
            text-[#838995] text-base
            hover:bg-primary hover:border-primary hover:text-white
            ">
            <span>
               <svg width="8" height="15" viewBox="0 0 8 15" class="fill-current stroke-current">
                  <path d="M0.870212 13.0861L0.870097 13.086L0.865602 13.0912C0.685237 13.3017 0.684716 13.6312 0.895299 13.8418C0.989374 13.9359 1.13704 13.9951 1.26387 13.9951C1.42264 13.9951 1.5463 13.9279 1.65431 13.8199L1.65436 13.82L1.65771 13.8164L7.16979 7.93248C7.16985 7.93243 7.1699 7.93237 7.16996 7.93231C7.59769 7.47923 7.59387 6.73477 7.17253 6.26385L7.17256 6.26382L7.17002 6.26111L1.65752 0.398611L1.65757 0.398563L1.65431 0.395299C1.454 0.194997 1.11779 0.150934 0.895299 0.373424C0.695526 0.573197 0.651169 0.908167 0.871667 1.13067L6.37922 6.98791C6.4442 7.06886 6.43141 7.17481 6.38592 7.2203L6.38587 7.22025L6.38271 7.22361L0.870212 13.0861Z" stroke-width="0.3"></path>
               </svg>
            </span>
         </a>
      </li>
   </ul>
</div>'''
    },{
    "html":'''<!DOCTYPE html>
<html>
    <head>
        <style data-href="https://fonts.googleapis.com/icon?family=Material+Icons">@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNa.woff) format('woff')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;font-feature-settings:'liga'}@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.woff2) format('woff2')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-feature-settings:'liga';-webkit-font-smoothing:antialiased}</style>
    </head>
    <body>
        <div class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible">
            <nav>
                <ul class="flex">
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Previous">
                            <span class="material-icons text-sm">keyboard_arrow_left</span>
                        </a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full bg-pink-500 p-0 text-sm text-white shadow-md transition duration-150 ease-in-out" href="#">1</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">2</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">3</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Next">
                            <span class="material-icons text-sm">keyboard_arrow_right</span>
                        </a>
                    </li>
                </ul>
            </nav>
            <div class="w-full md:w-7/12 pt-5 px-4 mb-8 mx-auto text-center">
                <div class="text-sm text-gray-700 py-1">
                This components requires
                <a
                    href="https://www.material-tailwind.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                    >Material Tailwind CSS & JS</a
                >
                for the classes. <br /><br />
                A component by<a
                    href="https://www.creative-tim.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                >
                    Creative Tim</a
                >.
                </div>
            </div>
      </div>
    </body>
</html>'''
    },{
    "html":'''<!DOCTYPE html>
<html>
    <head>
        <style data-href="https://fonts.googleapis.com/icon?family=Material+Icons">@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNa.woff) format('woff')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;font-feature-settings:'liga'}@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.woff2) format('woff2')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-feature-settings:'liga';-webkit-font-smoothing:antialiased}</style>
    </head>
    <body>
        <div class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible">
            <nav>
                <ul class="flex">
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Previous">
                            <span class="material-icons text-sm">keyboard_arrow_left</span>
                        </a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full bg-pink-500 p-0 text-sm text-white shadow-md transition duration-150 ease-in-out" href="#">1</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">2</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">3</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Next">
                            <span class="material-icons text-sm">keyboard_arrow_right</span>
                        </a>
                    </li>
                </ul>
            </nav>
            <div class="w-full md:w-7/12 pt-5 px-4 mb-8 mx-auto text-center">
                <div class="text-sm text-gray-700 py-1">
                This components requires
                <a
                    href="https://www.material-tailwind.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                    >Material Tailwind CSS & JS</a
                >
                for the classes. <br /><br />
                A component by<a
                    href="https://www.creative-tim.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                >
                    Creative Tim</a
                >.
                </div>
            </div>
      </div>
    </body>
</html>'''
    },{
    "html":'''<!DOCTYPE html>
<html>
    <head>
        <style data-href="https://fonts.googleapis.com/icon?family=Material+Icons">@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNa.woff) format('woff')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;font-feature-settings:'liga'}@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.woff2) format('woff2')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-feature-settings:'liga';-webkit-font-smoothing:antialiased}</style>
    </head>
    <body>
        <div class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible">
            <nav>
                <ul class="flex">
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Previous">
                            <span class="material-icons text-sm">keyboard_arrow_left</span>
                        </a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full bg-pink-500 p-0 text-sm text-white shadow-md transition duration-150 ease-in-out" href="#">1</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">2</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">3</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Next">
                            <span class="material-icons text-sm">keyboard_arrow_right</span>
                        </a>
                    </li>
                </ul>
            </nav>
            <div class="w-full md:w-7/12 pt-5 px-4 mb-8 mx-auto text-center">
                <div class="text-sm text-gray-700 py-1">
                This components requires
                <a
                    href="https://www.material-tailwind.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                    >Material Tailwind CSS & JS</a
                >
                for the classes. <br /><br />
                A component by<a
                    href="https://www.creative-tim.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                >
                    Creative Tim</a
                >.
                </div>
            </div>
      </div>
    </body>
</html>'''
    },{
    "html":'''<nav aria-label="Page navigation">
  <ul class="inline-flex space-x-2">
    <li><button class="flex items-center justify-center w-10 h-10 text-indigo-600 transition-colors duration-150 rounded-full focus:shadow-outline hover:bg-indigo-100">
      <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" fill-rule="evenodd"></path></svg></button>
    </li>
    <li><button class="w-10 h-10 text-indigo-600 transition-colors duration-150 rounded-full focus:shadow-outline hover:bg-indigo-100">1</button></li>
    <li><button class="w-10 h-10 text-indigo-600 transition-colors duration-150 rounded-full focus:shadow-outline hover:bg-indigo-100">2</button></li>
    <li><button class="w-10 h-10 text-white transition-colors duration-150 bg-indigo-600 border border-r-0 border-indigo-600 rounded-full focus:shadow-outline">3</button></li>
    <li><button class="flex items-center justify-center w-10 h-10 text-indigo-600 transition-colors duration-150 bg-white rounded-full focus:shadow-outline hover:bg-indigo-100">
      <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" fill-rule="evenodd"></path></svg></button>
    </li>
  </ul>
</nav>'''
    },{
    "html":'''<!-- This is an example component -->
<div class='flex items-center justify-center min-h-screen'>
  <div class="flex justify-center items-center space-x-4">
    <div class="border rounded-md bg-gray-100 px-2 py-1 text-3xl leading-6 text-slate-400 transition hover:bg-gray-200 hover:text-slate-500 cursor-pointer shadow-sm"><</div>
    <div class="text-slate-500">1 / 24</div>
    <div class="border rounded-md bg-gray-100 px-2 py-1 text-3xl leading-6 text-slate-400 transition hover:bg-gray-200 hover:text-slate-500 cursor-pointer shadow-sm">></div>
  </div>
</div>'''
    },{
    "html":'''<!-- This is an example component -->
<div class="max-w-2xl mx-auto">

	<nav aria-label="Page navigation example">
  <ul class="inline-flex items-center -space-x-px">
    <li>
      <a href="#" class="block py-2 px-3 ml-0 leading-tight text-gray-500 bg-white rounded-l-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
        <span class="sr-only">Previous</span>
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
      </a>
    </li>
    <li>
      <a href="#" class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">1</a>
    </li>
    <li>
      <a href="#" class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">2</a>
    </li>
    <li>
      <a href="#" aria-current="page" class="z-10 py-2 px-3 leading-tight text-blue-600 bg-blue-50 border border-blue-300 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">3</a>
    </li>
    <li>
      <a href="#" class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">4</a>
    </li>
    <li>
      <a href="#" class="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">5</a>
    </li>
    <li>
      <a href="#" class="block py-2 px-3 leading-tight text-gray-500 bg-white rounded-r-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
        <span class="sr-only">Next</span>
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
      </a>
    </li>
  </ul>
</nav>
	<p class="mt-5">This pagination component is part of a larger, open-source library of Tailwind CSS components. Learn more
		by going to the official <a class="text-blue-600 hover:underline"
			href="https://flowbite.com/docs/getting-started/introduction/" target="_blank">Flowbite Documentation</a>.
	</p>
</div>'''
    },{
    "html":'''<div class="flex justify-center">
  <nav aria-label="Page navigation example">
    <ul class="flex list-style-none">
      <li class="page-item disabled"><a
          class="page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none transition-all duration-300 rounded text-gray-500 pointer-events-none focus:shadow-none"
          href="#" tabindex="-1" aria-disabled="true">Previous</a></li>
      <li class="page-item"><a
          class="page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none transition-all duration-300 rounded text-gray-800 hover:text-gray-800 hover:bg-gray-200 focus:shadow-none"
          href="#">1</a></li>
      <li class="page-item active"><a
          class="page-link relative block py-1.5 px-3 rounded border-0 bg-blue-600 outline-none transition-all duration-300 rounded text-white hover:text-white hover:bg-blue-600 shadow-md focus:shadow-md"
          href="#">2 <span class="visually-hidden"></span></a></li>
      <li class="page-item"><a
          class="page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none transition-all duration-300 rounded text-gray-800 hover:text-gray-800 hover:bg-gray-200 focus:shadow-none"
          href="#">3</a></li>
      <li class="page-item"><a
          class="page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none transition-all duration-300 rounded text-gray-800 hover:text-gray-800 hover:bg-gray-200 focus:shadow-none"
          href="#">Next</a></li>
    </ul>
  </nav>
</div>'''
    },{
    "html":'''<!DOCTYPE html>
<html>
    <head>
        <style data-href="https://fonts.googleapis.com/icon?family=Material+Icons">@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNa.woff) format('woff')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;font-feature-settings:'liga'}@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v139/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.woff2) format('woff2')}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-feature-settings:'liga';-webkit-font-smoothing:antialiased}</style>
    </head>
    <body>
        <div class="grid min-h-[140px] w-full place-items-center overflow-x-scroll rounded-lg p-6 lg:overflow-visible">
            <nav>
                <ul class="flex">
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Previous">
                            <span class="material-icons text-sm">keyboard_arrow_left</span>
                        </a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full bg-gradient-to-tr from-pink-600 to-pink-400 p-0 text-sm text-white shadow-md shadow-pink-500/20 transition duration-150 ease-in-out" href="#">1</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">2</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#">3</a>
                    </li>
                    <li>
                        <a class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-light-300" href="#" aria-label="Next">
                            <span class="material-icons text-sm">keyboard_arrow_right</span>
                        </a>
                    </li>
                </ul>
            </nav>
            <div class="w-full md:w-7/12 pt-5 px-4 mb-8 mx-auto text-center">
                <div class="text-sm text-gray-700 py-1">
                This components requires
                <a
                    href="https://www.material-tailwind.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                    >Material Tailwind CSS & JS</a
                >
                for the classes. <br /><br />
                A component by<a
                    href="https://www.creative-tim.com?ref=tailwindcomponents"
                    class="text-gray-700 font-semibold"
                    target="_blank"
                >
                    Creative Tim</a
                >.
            </div>
        </div>
      </div>
    </body>
</html>'''
    }

]
Breadcrumb =[
    {
    "html":'''<!-- Breadcrumb -->
<nav class="flex bg-gray-50 text-gray-700 border border-gray-200 py-3 px-5 rounded-lg dark:bg-gray-800 dark:border-gray-700" aria-label="Breadcrumb">
  <ol class="inline-flex items-center space-x-1 md:space-x-3">
    <li class="inline-flex items-center">
      <a href="#" class="text-sm text-gray-700 hover:text-gray-900 inline-flex items-center dark:text-gray-400 dark:hover:text-white">
        <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
        Home
      </a>
    </li>
    <li>
      <div class="flex items-center">
        <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
        <a href="#" class="text-gray-700 hover:text-gray-900 ml-1 md:ml-2 text-sm font-medium dark:text-gray-400 dark:hover:text-white">Templates</a>
      </div>
    </li>
    <li aria-current="page">
      <div class="flex items-center">
        <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
        <span class="text-gray-400 ml-1 md:ml-2 text-sm font-medium dark:text-gray-500">Theme</span>
      </div>
    </li>
  </ol>
</nav>'''
    }
  
]
Accordions=[
    {
    "html":'''<!-- 
    FAQ - Frequently Asked Questions TailwindCSS Component
    with <details> and <summary> tag with custom [open] animation.
    Created by Surjith S M (@surjithctly)
    See more components: https://web3components.dev 
-->


<div class="max-w-screen-xl mx-auto px-5 bg-white min-h-sceen">
	<div class="flex flex-col items-center">
		<h2 class="font-bold text-5xl mt-5 tracking-tight">
			FAQ
		</h2>
		<p class="text-neutral-500 text-xl mt-3">
			Frequenty asked questions
		</p>
	</div>
	<div class="grid divide-y divide-neutral-200 max-w-xl mx-auto mt-8">
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> What is a SAAS platform?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					 SAAS platform is a cloud-based software service that allows users to access
					and use a variety of tools and functionality.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> How does  billing work?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					We offers a variety of billing options, including monthly and annual subscription plans,
					as well as pay-as-you-go pricing for certain services. Payment is typically made through a credit
					card or other secure online payment method.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> Can I get a refund for my subscription?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					We offers a 30-day money-back guarantee for most of its subscription plans. If you are not
					satisfied with your subscription within the first 30 days, you can request a full refund. Refunds
					for subscriptions that have been active for longer than 30 days may be considered on a case-by-case
					basis.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> How do I cancel my subscription?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					To cancel your We subscription, you can log in to your account and navigate to the
					subscription management page. From there, you should be able to cancel your subscription and stop
					future billing.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> Can I try this platform for free?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					We offers a free trial of its  platform for a limited time. During the trial period,
					you will have access to a limited set of features and functionality, but you will not be charged.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> How do I access   documentation?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					  Documentation is available on the company's website and can be accessed by
					logging in to your account. The documentation provides detailed information on how to use the ,
					as well as code examples and other resources.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> How do I contact support?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					If you need help with the platform or have any other questions, you can contact the
					company's support team by submitting a support request through the website or by emailing
					support@We.com.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> Do you offer any discounts or promotions?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					We may offer discounts or promotions from time to time. To stay up-to-date on the latest
					deals and special offers, you can sign up for the company's newsletter or follow it on social media.
				</p>
			</details>
		</div>
		<div class="py-5">
			<details class="group">
				<summary class="flex justify-between items-center font-medium cursor-pointer list-none">
					<span> How do we compare to other similar services?</span>
					<span class="transition group-open:rotate-180">
                <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
</svg>
              </span>
				</summary>
				<p class="text-neutral-600 mt-3 group-open:animate-fadeIn">
					 This platform is a highly reliable and feature-rich service that offers a wide range
					of tools and functionality. It is competitively priced and offers a variety of billing options to
					suit different needs and budgets.
				</p>
			</details>
		</div>
	</div>
</div>

<script>
	// ...
	// extend: {
    //   keyframes: {
    //     fadeIn: {
    //       "0%": { opacity: 0 },
    //       "100%": { opacity: 100 },
    //     },
    //   },
    //   animation: {
    //     fadeIn: "fadeIn 0.2s ease-in-out forwards",
    //   },
    // },
    // ...
</script>'''
    },{
    "html":'''<!-- This is an example component -->

<script defer src="https://unpkg.com/@alpinejs/collapse@3.x.x/dist/cdn.min.js"></script>
<script src="https://unpkg.com/alpinejs" defer></script>

<div class='flex items-center justify-center min-h-screen from-teal-100 via-teal-300 to-teal-500 bg-gradient-to-br' x-data="{ reportsOpen: false }">
    <div class='w-full max-w-lg px-10 py-8 mx-auto bg-white rounded-lg shadow-xl'>
        <div class='max-w-md mx-auto space-y-6'>
            <img src='https://tailwindcomponents.com/svg/logo-color.svg' class='h-8' />
    
            <p class='text-gray-600'></p>
    
            <div @click="reportsOpen = !reportsOpen" class='flex items-center text-gray-600 w-full border-b overflow-hidden mt-32 md:mt-0 mb-5 mx-auto'>
            <div class='w-10 border-r px-2 transform transition duration-300 ease-in-out' :class="{'rotate-90': reportsOpen,' -translate-y-0.0': !reportsOpen }">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
            </svg>          
            </div>
            <div class='flex items-center px-2 py-3'>
            <div class='mx-3'>
                <button class="hover:underline">This is where you click to open</button>
            </div>
            </div>
            </div>

            <div class="flex p-5 md:p-0 w-full transform transition duration-300 ease-in-out border-b pb-10"
            x-cloak x-show="reportsOpen" x-collapse x-collapse.duration.500ms >
            This is a very simple dropdown/accordion/collapse (whatever you call it) using Tailwind, Alpine.js, and the Alpine.js plugin "Collapse" to enable smoother open/collapse transitions than what comes out of the box with Alpine.js
            </div>

        </div>
    </div>
</div>'''
    },{
    "html":'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <script
      src="https://kit.fontawesome.com/4a314d7cd5.js"
      crossorigin="anonymous"
    ></script>
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins&display=swap"
      rel="stylesheet"
    />
    <script src="https://cdn.tailwindcss.com"></script>
    <style type="text/tailwindcss">
      * {
        font-family: "Poppins", sans-serif;
      }
      @layer components {
        .item {
          @apply w-full sm:w-96 text-xs sm:text-sm flex items-center gap-x-3 flex-wrap select-none;
        }
        .content {
          @apply peer-checked:max-h-max max-h-0 basis-full peer-checked:border-y-[1px] border-blue-300 peer-checked:p-3 overflow-hidden transition-all select-text;
        }
      }
    </style>
  </head>
  <body
    class="grid place-content-center h-screen bg-gradient-to-bl from-cyan-200 via-sky-300 to-blue-400"
  >
    <ul class="text-white shadow-2xl">
      <!-- single Accordion -->
      <li class="bg-indigo-500 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq1" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq1" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>What is your name?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>My name is Sohan Emon</p>
        </div>
      </li>
      <li class="bg-sky-500 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq2" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq2" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>What do you do?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>I'm a fullstack web developer.</p>
        </div>
      </li>
      <li class="bg-blue-500 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq3" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq3" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>What is your favorite stack?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>Next, Tailwind CSS, Node, MongoDB</p>
        </div>
      </li>
      <li class="bg-cyan-600 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq4" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq4" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>Do you have a portfolio?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>
            Go,
            <a
              class="text-blue-100 hover:underline underline-offset-2"
              target="_blank"
              href="https://onemanse.vercel.app"
              >there</a
            >
          </p>
        </div>
      </li>
    </ul>
  </body>
</html>'''
    },{
    "html":'''<!-- This is an example component -->

<script defer src="https://unpkg.com/@alpinejs/collapse@3.x.x/dist/cdn.min.js"></script>
<script src="https://unpkg.com/alpinejs" defer></script>

<div class='flex items-center justify-center min-h-screen from-teal-100 via-teal-300 to-teal-500 bg-gradient-to-br' x-data="{ reportsOpen: false }">
    <div class='w-full max-w-lg px-10 py-8 mx-auto bg-white rounded-lg shadow-xl'>
        <div class='max-w-md mx-auto space-y-6'>
            <img src='https://tailwindcomponents.com/svg/logo-color.svg' class='h-8' />
    
            <p class='text-gray-600'></p>
    
            <div @click="reportsOpen = !reportsOpen" class='flex items-center text-gray-600 w-full border-b overflow-hidden mt-32 md:mt-0 mb-5 mx-auto'>
            <div class='w-10 border-r px-2 transform transition duration-300 ease-in-out' :class="{'rotate-90': reportsOpen,' -translate-y-0.0': !reportsOpen }">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
            </svg>          
            </div>
            <div class='flex items-center px-2 py-3'>
            <div class='mx-3'>
                <button class="hover:underline">This is where you click to open</button>
            </div>
            </div>
            </div>

            <div class="flex p-5 md:p-0 w-full transform transition duration-300 ease-in-out border-b pb-10"
            x-cloak x-show="reportsOpen" x-collapse x-collapse.duration.500ms >
            This is a very simple dropdown/accordion/collapse (whatever you call it) using Tailwind, Alpine.js, and the Alpine.js plugin "Collapse" to enable smoother open/collapse transitions than what comes out of the box with Alpine.js
            </div>

        </div>
    </div>
</div>'''
    
    },{
    "html":'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <script
      src="https://kit.fontawesome.com/4a314d7cd5.js"
      crossorigin="anonymous"
    ></script>
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins&display=swap"
      rel="stylesheet"
    />
    <script src="https://cdn.tailwindcss.com"></script>
    <style type="text/tailwindcss">
      * {
        font-family: "Poppins", sans-serif;
      }
      @layer components {
        .item {
          @apply w-full sm:w-96 text-xs sm:text-sm flex items-center gap-x-3 flex-wrap select-none;
        }
        .content {
          @apply peer-checked:max-h-max max-h-0 basis-full peer-checked:border-y-[1px] border-blue-300 peer-checked:p-3 overflow-hidden transition-all select-text;
        }
      }
    </style>
  </head>
  <body
    class="grid place-content-center h-screen bg-gradient-to-bl from-cyan-200 via-sky-300 to-blue-400"
  >
    <ul class="text-white shadow-2xl">
      <!-- single Accordion -->
      <li class="bg-indigo-500 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq1" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq1" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>What is your name?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>My name is Sohan Emon</p>
        </div>
      </li>
      <li class="bg-sky-500 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq2" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq2" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>What do you do?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>I'm a fullstack web developer.</p>
        </div>
      </li>
      <li class="bg-blue-500 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq3" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq3" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>What is your favorite stack?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>Next, Tailwind CSS, Node, MongoDB</p>
        </div>
      </li>
      <li class="bg-cyan-600 item">
        <!-- wrap is important here -->
        <input type="checkbox" id="faq4" class="peer appearance-none" />
        <i class="fa-solid fa-chevron-right peer-checked:hidden inline"></i>
        <i class="fa-solid fa-chevron-down peer-checked:inline hidden"></i>
        <label for="faq4" class="py-4 cursor-pointer grow">
          <!-- note: grow is used to fill all remaining space of the article -->
          <p>Do you have a portfolio?</p></label
        >
        <!-- note: checkbox will be triggered even if label is triggered. -->
        <div class="content">
          <!-- note: basis may not work without wrap -->
          <p>
            Go,
            <a
              class="text-blue-100 hover:underline underline-offset-2"
              target="_blank"
              href="https://onemanse.vercel.app"
              >there</a
            >
          </p>
        </div>
      </li>
    </ul>
  </body>
</html>'''
    },{
    "html":'''<!--

This is a pure css accordian that uses a checkbox state 
to determine if the accordian is expanded or collapsed.

In theory you can use radio inputs bound to the same name
to create self collapsing accordian.

Accessibility considerations:
    1. There is not aria-expanded for css
    2. An aria-describedby would help bind the input and label to the div containing the description
    3. There should be some consideration for reduced motion i.e. `motion-safe:transition-all`


SVG is from heroicons.com
-->

<div class="flex flex-wrap justify-start overflow-hidden bg-slate-900 text-white">
  <label class="grow px-4 py-3 font-medium" for="collapse">Who?</label>
  <input class="peer mx-4 my-3 h-0 w-0 appearance-none rounded border text-slate-800 accent-slate-600 opacity-0" type="checkbox" name="collapse" id="collapse" />
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mx-4 my-3 h-6 w-6 transition-all duration-200 peer-checked:rotate-45">
    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6" />
  </svg>
  <div class="-transparent absolute -translate-y-full scale-75 scale-y-0 px-4 py-3 opacity-0 transition-all duration-200 peer-checked:relative peer-checked:translate-y-0 peer-checked:scale-100 peer-checked:scale-y-100 peer-checked:bg-slate-800 peer-checked:opacity-100">
      We don’t serve their kind here! What? Your droids. They’ll have to wait outside. We don’t want them here. Listen, why don’t you wait out by the speeder. We don’t want any trouble. I heartily agree with you sir. Negola dewaghi wooldugger?!? He doesn’t like you. I’m sorry. I don’t like you either You just watch yourself. We’re wanted men. I have the death sentence in twelve systems. I’ll be careful than. You’ll be dead. This little one isn’t worth the effort. Come let me buy you something…
  </div>
</div>



<div class="flex flex-wrap justify-start overflow-hidden bg-slate-900 text-white">
  <label class="grow px-4 py-3 font-medium" for="collapse2">How?</label>
  <input class="peer mx-4 my-3 h-0 w-0 appearance-none rounded border text-slate-800 accent-slate-600 opacity-0" type="checkbox" name="collapse2" id="collapse2" />
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mx-4 my-3 h-6 w-6 transition-all duration-200 peer-checked:rotate-45">
    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6" />
  </svg>
  <div class="-transparent absolute -translate-y-full scale-75 scale-y-0 px-4 py-3 opacity-0 transition-all duration-200 peer-checked:relative peer-checked:translate-y-0 peer-checked:scale-100 peer-checked:scale-y-100 peer-checked:bg-slate-800 peer-checked:opacity-100">The approach will not be easy. You are required to maneuver straight down this trench and skim the surface to this point. The target area is only two meters wide. It’s a small thermal exhaust port, right below the main port. The shaft leads directly to the reactor system. A precise hit will start a chain reaction which should destroy the station. Only a precise hit will set up a chain reaction. The shaft is ray-shielded, so you’ll have to use proton torpedoes. That’s impossible, even for a computer. It’s not impossible. I used to bull’s-eye womp rats in my T-sixteen back home. They’re not much bigger than two meters. Man your ships! And may the Force be with you!</div>
</div>




<!-- Ingore this -->
<style>
    body {
        height: 100%;
        padding: 4rem;        
    }
</style>'''
    }

]
Dashboard =[
    {
    "html":'''<link rel="preconnect" href="https://rsms.me/">
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
<style>
    :root { font-family: 'Inter', sans-serif; }
@supports (font-variation-settings: normal) {
  :root { font-family: 'Inter var', sans-serif; }
}
</style>
<div class="bg-slate-100 overflow-y-scroll w-screen h-screen antialiased text-slate-300 selection:bg-blue-600 selection:text-white">
    <div class="flex flex-col relative w-screen">
        <div id="menu" class="bg-gray-900 min-h-screen z-10 text-slate-300 w-64 fixed left-0 h-screen overflow-y-scroll">
           <div id="logo" class="my-4 px-6">
            <h1 class="text-lg md:text-2xl font-bold text-white">Dash<span class="text-blue-500">8</span>.</h1>
            <p class="text-slate-500 text-sm">Manage your actions and activities</p>
           </div>
           <div id="profile" class="px-6 py-10">
            <p class="text-slate-500">Welcome back,</p>
            <a href="#" class="inline-flex space-x-2 items-center">
                <span>
                    <img class="rounded-full w-8 h-8" src="https://images.unsplash.com/photo-1542909168-82c3e7fdca5c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=128&q=80" alt="">
                </span>
                <span class="text-sm md:text-base font-bold">
                    Edward Tompson
                </span>
                </a>
           </div>
           <div id="nav" class="w-full px-6">
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 bg-blue-800 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-white">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z" />
                      </svg>
                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg font-bold leading-5 text-white">Dashboard</span>
                    <span class="text-sm text-white/50 hidden md:block">Data Overview</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" />
                      </svg>                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Database</span>
                    <span class="text-sm text-slate-500 hidden md:block">Database Manager</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15a4.5 4.5 0 004.5 4.5H18a3.75 3.75 0 001.332-7.257 3 3 0 00-3.758-3.848 5.25 5.25 0 00-10.233 2.33A4.502 4.502 0 002.25 15z" />
                      </svg>                        
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Cloud Storage</span>
                    <span class="text-sm text-slate-500 hidden md:block">Manage Cloud Storage</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3 3v1.5M3 21v-6m0 0l2.77-.693a9 9 0 016.208.682l.108.054a9 9 0 006.086.71l3.114-.732a48.524 48.524 0 01-.005-10.499l-3.11.732a9 9 0 01-6.085-.711l-.108-.054a9 9 0 00-6.208-.682L3 4.5M3 15V4.5" />
                      </svg>                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Reports</span>
                    <span class="text-sm text-slate-500 hidden md:block">Manage Reports</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" />
                      </svg>                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Security</span>
                    <span class="text-sm text-slate-500 hidden md:block">Generate Security Keys</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 7.125C2.25 6.504 2.754 6 3.375 6h6c.621 0 1.125.504 1.125 1.125v3.75c0 .621-.504 1.125-1.125 1.125h-6a1.125 1.125 0 01-1.125-1.125v-3.75zM14.25 8.625c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v8.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-8.25zM3.75 16.125c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-2.25z" />
                      </svg>                                          
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Extensions</span>
                    <span class="text-sm text-slate-500 hidden md:block">Manage Extensions</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12a7.5 7.5 0 0015 0m-15 0a7.5 7.5 0 1115 0m-15 0H3m16.5 0H21m-1.5 0H12m-8.457 3.077l1.41-.513m14.095-5.13l1.41-.513M5.106 17.785l1.15-.964m11.49-9.642l1.149-.964M7.501 19.795l.75-1.3m7.5-12.99l.75-1.3m-6.063 16.658l.26-1.477m2.605-14.772l.26-1.477m0 17.726l-.26-1.477M10.698 4.614l-.26-1.477M16.5 19.794l-.75-1.299M7.5 4.205L12 12m6.894 5.785l-1.149-.964M6.256 7.178l-1.15-.964m15.352 8.864l-1.41-.513M4.954 9.435l-1.41-.514M12.002 12l-3.75 6.495" />
                      </svg>                                        
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Settings</span>
                    <span class="text-sm text-slate-500 hidden md:block">Edit App Settings</span>
                </div>
            </a>
            
           </div>
        </div>
        
      
    </div>
</div>'''
    },{
    "html":'''<link rel="preconnect" href="https://rsms.me/">
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
<style>
    :root { font-family: 'Inter', sans-serif; }
@supports (font-variation-settings: normal) {
  :root { font-family: 'Inter var', sans-serif; }
}
</style>

<div class="antialiased bg-black w-full min-h-screen text-slate-300 relative py-4">
    <div class="grid grid-cols-12 mx-auto gap-2 sm:gap-4 md:gap-6 lg:gap-10 xl:gap-14 max-w-7xl my-10 px-2">
        <div id="menu" class="bg-white/10 col-span-3 rounded-lg p-4 ">
            <h1 class="font-bold text-lg lg:text-3xl bg-gradient-to-br from-white via-white/50 to-transparent bg-clip-text text-transparent">Dashboard<span class="text-indigo-400">.</span></h1>
            <p class="text-slate-400 text-sm mb-2">Welcome back,</p>
            <a href="#" class="flex flex-col space-y-2 md:space-y-0 md:flex-row mb-5 items-center md:space-x-2 hover:bg-white/10 group transition duration-150 ease-linear rounded-lg group w-full py-3 px-2">
                <div>
                    <img class="rounded-full w-10 h-10 relative object-cover" src="https://img.freepik.com/free-photo/no-problem-concept-bearded-man-makes-okay-gesture-has-everything-control-all-fine-gesture-wears-spectacles-jumper-poses-against-pink-wall-says-i-got-this-guarantees-something_273609-42817.jpg?w=1800&t=st=1669749937~exp=1669750537~hmac=4c5ab249387d44d91df18065e1e33956daab805bee4638c7fdbf83c73d62f125" alt="">
                </div>
                <div>
                    <p class="font-medium group-hover:text-indigo-400 leading-4">Jim Smith</p>
                    <span class="text-xs text-slate-400">Pantazi LLC</span>
                </div>
            </a>
            <hr class="my-2 border-slate-700">
            <div id="menu" class="flex flex-col space-y-2 my-5">
                <a href="#" class="hover:bg-white/10 transition duration-150 ease-linear rounded-lg py-3 px-2 group">
                    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 space-x-2 items-center">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 group-hover:text-indigo-400">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                              </svg>
                              
                        </div>
                        <div>
                            <p class="font-bold text-base lg:text-lg text-slate-200 leading-4 group-hover:text-indigo-400">Dashboard</p>
                        <p class="text-slate-400 text-sm hidden md:block">Data overview</p>
                        </div>
                        
                    </div>
                </a>
                <a href="#" class="hover:bg-white/10 transition duration-150 ease-linear rounded-lg py-3 px-2 group">
                    <div class="relative flex flex-col space-y-2 md:flex-row md:space-y-0 space-x-2 items-center">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 group-hover:text-indigo-400">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
                              </svg>                              
                        </div>
                        <div>
                            <p class="font-bold text-base lg:text-lg text-slate-200 leading-4 group-hover:text-indigo-400">Invoices</p>
                        <p class="text-slate-400 text-sm hidden md:block">Manage invoices</p>
                        </div>
                        <div class="absolute -top-3 -right-3 md:top-0 md:right-0 px-2 py-1.5 rounded-full bg-indigo-800 text-xs font-mono font-bold">23</div>
                    </div>
                </a>
                <a href="#" class="hover:bg-white/10 transition duration-150 ease-linear rounded-lg py-3 px-2 group">
                    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 space-x-2 items-center">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 group-hover:text-indigo-400">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" />
                              </svg>                              
                        </div>
                        <div>
                            <p class="font-bold text-base lg:text-lg text-slate-200 leading-4 group-hover:text-indigo-400">Users</p>
                        <p class="text-slate-400 text-sm hidden md:block">Manage users</p>
                        </div>
                        
                    </div>
                </a>
                <a href="#" class="hover:bg-white/10 transition duration-150 ease-linear rounded-lg py-3 px-2 group">
                    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 space-x-2 items-center">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 group-hover:text-indigo-400">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.324.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.613-.431.992a6.759 6.759 0 010 .255c-.007.378.138.75.43.99l1.005.828c.424.35.534.954.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.28c-.09.543-.56.941-1.11.941h-2.594c-.55 0-1.02-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.992a6.932 6.932 0 010-.255c.007-.378-.138-.75-.43-.99l-1.004-.828a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.087.22-.128.332-.183.582-.495.644-.869l.214-1.281z" />
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                              </svg>
                                
                        </div>
                        <div>
                            <p class="font-bold text-base lg:text-lg text-slate-200 leading-4 group-hover:text-indigo-400">Settings</p>
                        <p class="text-slate-400 text-sm hidden md:block">Edit settings</p>
                        </div>
                        
                    </div>
                </a>
            </div>
            <p class="text-sm text-center text-gray-600">v2.0.0.3 | &copy; 2022 Pantazi Soft</p>
        </div>
        <div id="content" class="bg-white/10 col-span-9 rounded-lg p-6">
            <div id="24h">
                <h1 class="font-bold py-4 uppercase">Last 24h Statistics</h1>
                <div id="stats" class="grid gird-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="bg-black/60 to-white/5 p-6 rounded-lg">
                        <div class="flex flex-row space-x-4 items-center">
                            <div id="stats-1">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10 text-white">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" />
                                  </svg>
                            </div>
                            <div>
                                <p class="text-indigo-300 text-sm font-medium uppercase leading-4">Users</p>
                                <p class="text-white font-bold text-2xl inline-flex items-center space-x-2">
                                    <span>+28</span>
                                    <span>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" />
                                          </svg>
                                          
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="bg-black/60 p-6 rounded-lg">
                        <div class="flex flex-row space-x-4 items-center">
                            <div id="stats-1">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10 text-white">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                  </svg>
                                  
                            </div>
                            <div>
                                <p class="text-teal-300 text-sm font-medium uppercase leading-4">Income</p>
                                <p class="text-white font-bold text-2xl inline-flex items-center space-x-2">
                                    <span>$2,873.88</span>
                                    <span>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" />
                                          </svg>
                                          
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="bg-black/60 p-6 rounded-lg">
                        <div class="flex flex-row space-x-4 items-center">
                            <div id="stats-1">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10 text-white">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
                                  </svg>
                                  
                            </div>
                            <div>
                                <p class="text-blue-300 text-sm font-medium uppercase leading-4">Invoices</p>
                                <p class="text-white font-bold text-2xl inline-flex items-center space-x-2">
                                    <span>+79</span>
                                    <span>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" />
                                          </svg>
                                          
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div id="last-incomes">
                <h1 class="font-bold py-4 uppercase">Last 24h incomes</h1>
                <div id="stats" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                    <div class="bg-black/60 to-white/5 rounded-lg">
                            <div class="flex flex-row items-center">
                                <div class="text-3xl p-4">💰</div>
                                <div class="p-2">
                                    <p class="text-xl font-bold">348$</p>
                                    <p class="text-gray-500 font-medium">Amber Gates</p>
                                    <p class="text-gray-500 text-sm">24 Nov 2022</p>
                                </div>
                            </div>
                            <div class="border-t border-white/5 p-4">
                                <a href="#" class="inline-flex space-x-2 items-center text-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                                      </svg>
                                      <span>Info</span>                                      
                                </a>
                            </div>
                    </div>
                    <div class="bg-black/60 to-white/5 rounded-lg">
                        <div class="flex flex-row items-center">
                            <div class="text-3xl p-4">💰</div>
                            <div class="p-2">
                                <p class="text-xl font-bold">68$</p>
                                <p class="text-gray-500 font-medium">Maia Kipper</p>
                                <p class="text-gray-500 text-sm">23 Nov 2022</p>
                            </div>
                        </div>
                        <div class="border-t border-white/5 p-4">
                            <a href="#" class="inline-flex space-x-2 items-center text-center">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                                  </svg>
                                  <span>Info</span>                                      
                            </a>
                        </div>
                </div>
                <div class="bg-black/60 to-white/5 rounded-lg">
                    <div class="flex flex-row items-center">
                        <div class="text-3xl p-4">💰</div>
                        <div class="p-2">
                            <p class="text-xl font-bold">12$</p>
                            <p class="text-gray-500 font-medium">Oprah Milles</p>
                            <p class="text-gray-500 text-sm">23 Nov 2022</p>
                        </div>
                    </div>
                    <div class="border-t border-white/5 p-4">
                        <a href="#" class="inline-flex space-x-2 items-center text-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                              </svg>
                              <span>Info</span>                                      
                        </a>
                    </div>
            </div>
            <div class="bg-black/60 to-white/5 rounded-lg">
                <div class="flex flex-row items-center">
                    <div class="text-3xl p-4">💰</div>
                    <div class="p-2">
                        <p class="text-xl font-bold">105$</p>
                        <p class="text-gray-500 font-medium">Jonny Nite</p>
                        <p class="text-gray-500 text-sm">23 Nov 2022</p>
                    </div>
                </div>
                <div class="border-t border-white/5 p-4">
                    <a href="#" class="inline-flex space-x-2 items-center text-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                          </svg>
                          <span>Info</span>                                      
                    </a>
                </div>
        </div>
        <div class="bg-black/60 to-white/5 rounded-lg">
            <div class="flex flex-row items-center">
                <div class="text-3xl p-4">💰</div>
                <div class="p-2">
                    <p class="text-xl font-bold">52$</p>
                    <p class="text-gray-500 font-medium">Megane Baile</p>
                    <p class="text-gray-500 text-sm">22 Nov 2022</p>
                </div>
            </div>
            <div class="border-t border-white/5 p-4">
                <a href="#" class="inline-flex space-x-2 items-center text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                      </svg>
                      <span>Info</span>                                      
                </a>
            </div>
    </div>
    <div class="bg-black/60 to-white/5 rounded-lg">
        <div class="flex flex-row items-center">
            <div class="text-3xl p-4">💰</div>
            <div class="p-2">
                <p class="text-xl font-bold">28$</p>
                <p class="text-gray-500 font-medium">Tony Ankel</p>
                <p class="text-gray-500 text-sm">22 Nov 2022</p>
            </div>
        </div>
        <div class="border-t border-white/5 p-4">
            <a href="#" class="inline-flex space-x-2 items-center text-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                  </svg>
                  <span>Info</span>                                      
            </a>
        </div>
</div>
                </div>
            </div>
            <div id="last-users">
                <h1 class="font-bold py-4 uppercase">Last 24h users</h1>
                <div class="overflow-x-scroll">
                    <table class="w-full whitespace-nowrap">
                        <thead class="bg-black/60">
                            <th class="text-left py-3 px-2 rounded-l-lg">Name</th>
                            <th class="text-left py-3 px-2">Email</th>
                            <th class="text-left py-3 px-2">Group</th>
                            <th class="text-left py-3 px-2">Status</th>
                            <th class="text-left py-3 px-2 rounded-r-lg">Actions</th>
                        </thead>
                        <tr class="border-b border-gray-700">
                            <td class="py-3 px-2 font-bold">
                                <div class="inline-flex space-x-3 items-center">
                                    <span><img class="rounded-full w-8 h-8" src="https://images.generated.photos/tGiLEDiAbS6NdHAXAjCfpKoW05x2nq70NGmxjxzT5aU/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTM4ODM1LmpwZw.jpg" alt=""></span>
                                    <span>Thai Mei</span>
                                </div>
                            </td>
                            <td class="py-3 px-2">thai.mei@abc.com</td>
                            <td class="py-3 px-2">User</td>
                            <td class="py-3 px-2">Approved</td>
                            <td class="py-3 px-2">
                                <div class="inline-flex items-center space-x-3">
                                    <a href="" title="Edit" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                                      </svg>
                                      </a>
                                    <a href="" title="Edit password" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                                      </svg>
                                      </a>
                                    <a href="" title="Suspend user" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                                      </svg>
                                      </a>
                                </div>
                            </td>
                        </tr>
                        <tr class="border-b border-gray-700">
                            <td class="py-3 px-2 font-bold">
                                <div class="inline-flex space-x-3 items-center">
                                    <span><img class="rounded-full w-8 h-8" src="https://images.generated.photos/tGiLEDiAbS6NdHAXAjCfpKoW05x2nq70NGmxjxzT5aU/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTM4ODM1LmpwZw.jpg" alt=""></span>
                                    <span>Thai Mei</span>
                                </div>
                            </td>
                            <td class="py-3 px-2">thai.mei@abc.com</td>
                            <td class="py-3 px-2">User</td>
                            <td class="py-3 px-2">Approved</td>
                            <td class="py-3 px-2">
                                <div class="inline-flex items-center space-x-3">
                                    <a href="" title="Edit" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                                      </svg>
                                      </a>
                                    <a href="" title="Edit password" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                                      </svg>
                                      </a>
                                    <a href="" title="Suspend user" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                                      </svg>
                                      </a>
                                </div>
                            </td>
                        </tr>
                        <tr class="border-b border-gray-700">
                            <td class="py-3 px-2 font-bold">
                                <div class="inline-flex space-x-3 items-center">
                                    <span><img class="rounded-full w-8 h-8" src="https://images.generated.photos/tGiLEDiAbS6NdHAXAjCfpKoW05x2nq70NGmxjxzT5aU/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTM4ODM1LmpwZw.jpg" alt=""></span>
                                    <span>Thai Mei</span>
                                </div>
                            </td>
                            <td class="py-3 px-2">thai.mei@abc.com</td>
                            <td class="py-3 px-2">User</td>
                            <td class="py-3 px-2">Approved</td>
                            <td class="py-3 px-2">
                                <div class="inline-flex items-center space-x-3">
                                    <a href="" title="Edit" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                                      </svg>
                                      </a>
                                    <a href="" title="Edit password" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                                      </svg>
                                      </a>
                                    <a href="" title="Suspend user" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                                      </svg>
                                      </a>
                                </div>
                            </td>
                        </tr>
                        <tr class="border-b border-gray-700">
                            <td class="py-3 px-2 font-bold">
                                <div class="inline-flex space-x-3 items-center">
                                    <span><img class="rounded-full w-8 h-8" src="https://images.generated.photos/niCVbIBAm4hahzwS83HoEtcVEIactkKohOzgXWYY4lM/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NTk4ODczLmpwZw.jpg" alt=""></span>
                                    <span>Marquez Spineli</span>
                                </div>
                            </td>
                            <td class="py-3 px-2">marquez.spineli@cba.com</td>
                            <td class="py-3 px-2">User</td>
                            <td class="py-3 px-2">Approved</td>
                            <td class="py-3 px-2">
                                <div class="inline-flex items-center space-x-3">
                                    <a href="" title="Edit" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                                      </svg>
                                      </a>
                                    <a href="" title="Edit password" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                                      </svg>
                                      </a>
                                    <a href="" title="Suspend user" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                                      </svg>
                                      </a>
                                </div>
                            </td>
                        </tr>
                        <tr class="border-b border-gray-800">
                            <td class="py-3 px-2 font-bold">
                                <div class="inline-flex space-x-3 items-center">
                                    <span><img class="rounded-full w-8 h-8" src="https://images.generated.photos/f_xU7q780YXiKG7IwKVV05eU6Sj2nIodEkN1S8GyM2M/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NDk2MTc4LmpwZw.jpg" alt=""></span>
                                    <span>Mark Spike</span>
                                </div>
                            </td>
                            <td class="py-3 px-2">mark.spike@abc.com</td>
                            <td class="py-3 px-2">Administrator</td>
                            <td class="py-3 px-2">Approved</td>
                            <td class="py-3 px-2">
                                <div class="inline-flex items-center space-x-3">
                                    <a href="" title="Edit" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                                      </svg>
                                      </a>
                                    <a href="" title="Edit password" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                                      </svg>
                                      </a>
                                    <a href="" title="Suspend user" class="hover:text-white"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
                                      </svg>
                                      </a>
                                </div>
                            </td>
                        </tr>

                        
                    </table>
                </div>
            </div>
           
        </div>
    </div>
</div>'''
    }
  ,{
    "html":'''<div class="w-full bg-white shadow-xl rounded-lg flex overflow-x-auto custom-scrollbar">
                        <div class="w-64 px-4">
                            <div class="h-16 flex items-center">
                                <a href="#" class="w-48 mx-auto bg-blue-500 hover:bg-blue-700 flex items-center justify-center text-gray-100 py-2 rounded space-x-2 transition duration-150">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                                    </svg>
                                    <span>Compose</span>
                                </a>
                            </div>
                            <div class="px-2 pt-4 pb-8 border-r border-gray-300">
                                <ul class="space-y-2">
                                    <li>
                                        <a class="bg-gray-500 bg-opacity-30 text-blue-500 flex items-center justify-between py-1.5 px-4 rounded cursor-pointer">
                                            <span class="flex items-center space-x-2">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path>
                                                </svg>
                                                <span>Inbox</span>
                                            </span>
                                            <span class="bg-sky-500 text-gray-100 font-bold px-2 py-0.5 text-xs rounded-lg">3</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-500 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                            </svg>
                                            <span>Starred</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-500 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                            </svg>
                                            <span>Snoozed</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-500 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                            </svg>
                                            <span>Important</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-500 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
                                            </svg>
                                            <span>Sent</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-500 flex items-center justify-between text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                                            <span class="flex items-center space-x-2">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                                                </svg>
                                                <span>Drafts</span>
                                            </span>
                                            <span class="bg-sky-500 text-gray-100 font-bold px-2 py-0.5 text-xs rounded-lg">1</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-500 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                                            </svg>
                                            <span>Spam</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-500 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                            </svg>
                                            <span>Trash</span>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="flex-1 px-2">
                            <div class="h-16 flex items-center">
                                <h4 class="text-lg font-bold">New Message</h4>
                            </div>
                            <div class="mb-6 pt-4">
                                <div>
                                    <input type="text" name="to" id="to" class="w-full text-gray-700 py-1 border-b border-b-gray-300 focus:outline-none focus:ring-0 focus:border-transparent focus:border-b-gray-300" placeholder="To">
                                </div>
                                <div>
                                    <input type="text" name="cc" id="cc" class="w-full text-gray-700 py-1 border-b border-b-gray-300 focus:outline-none focus:ring-0 focus:border-transparent focus:border-b-gray-300" placeholder="Cc">
                                </div>
                                <div>
                                    <input type="text" name="bcc" id="bcc" class="w-full text-gray-700 py-1 border-b border-b-gray-300 focus:outline-none focus:ring-0 focus:border-transparent focus:border-b-gray-300" placeholder="Bcc">
                                </div>
                                <div>
                                    <textarea id="body" class="w-full h-64 text-gray-700 border-b border-b-gray-300 focus:outline-none focus:ring-0 focus:border-transparent focus:border-b-gray-300" placeholder="Message..."></textarea>
                                </div>
                                <div class="flex items-center space-x-2 my-2">
                                    <div class="w-40 flex items-center justify-between text-gray-600 px-2 py-1.5  border border-gray-400 rounded-lg hover:bg-gray-200">
                                        <div class="w-28 flex items-center space-x-1">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path>
                                            </svg>
                                            <span class="text-sm truncate">Review.zip</span>
                                        </div>
                                        <button class="hover:text-gray-900" title="Remove">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                                            </svg>
                                        </button>
                                    </div>
                                    <div class="w-40 flex items-center justify-between text-gray-600 px-2 py-1.5  border border-gray-400 rounded-lg hover:bg-gray-200">
                                        <div class="w-28 flex items-center space-x-1">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path>
                                            </svg>
                                            <span class="text-sm truncate">Approve.zip</span>
                                        </div>
                                        <button class="hover:text-gray-900" title="Remove">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                                <div class="flex items-center justify-between mt-4">
                                    <div class="flex items-center space-x-2">
                                        <button class="bg-blue-500 hover:bg-blue-700 rounded-lg px-12 py-1.5 text-gray-100 hover:shadow-xl transition duration-150">Send</button>
                                        <button title="Attach Files">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-500 hover:text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"></path>
                                            </svg>
                                        </button>
                                    </div>
                                    <button class="mr-4 text-gray-700 hover:text-gray-900" title="Delete">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>'''
  },{
    "html":'''<link rel="stylesheet" href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css">
<link rel="stylesheet" href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css">

<div class="flex flex-wrap bg-pink-500 ">
    <div class="mt-4 w-full lg:w-6/12 xl:w-3/12 px-5 mb-4">
    <div class="relative flex flex-col min-w-0 break-words bg-white rounded mb-3 xl:mb-0 shadow-lg">
        <div class="flex-auto p-4">
        <div class="flex flex-wrap">
            <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
            <h5 class="text-blueGray-400 uppercase font-bold text-xs"> Traffic</h5>
            <span class="font-semibold text-xl text-blueGray-700">334,100</span>
            </div>
            <div class="relative w-auto pl-4 flex-initial">
            <div class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full  bg-red-500">
                <i class="fas fa-chart-bar"></i>
            </div>
            </div>
        </div>
        <p class="text-sm text-blueGray-400 mt-4">
            <span class="text-emerald-500 mr-2"><i class="fas fa-arrow-up"></i> 2,99% </span>
            <span class="whitespace-nowrap"> Since last month </span></p>
        </div>
    </div>
    </div>

    <div class=" mt-4 w-full lg:w-6/12 xl:w-3/12 px-5">
    <div class="relative flex flex-col min-w-0 break-words bg-white rounded mb-4 xl:mb-0 shadow-lg">
        <div class="flex-auto p-4">
        <div class="flex flex-wrap">
            <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
            <h5 class="text-blueGray-400 uppercase font-bold text-xs">New users</h5>
            <span class="font-semibold text-xl text-blueGray-700">2,999</span>
            </div>
            <div class="relative w-auto pl-4 flex-initial">
            <div class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full  bg-pink-500">
                <i class="fas fa-chart-pie"></i>
            </div>
            </div>
        </div>
        <p class="text-sm text-blueGray-400 mt-4">
            <span class="text-red-500 mr-2"><i class="fas fa-arrow-down"></i> 4,01%</span>
            <span class="whitespace-nowrap"> Since last week </span></p>
        </div>
    </div>
    </div>

    <div class="mt-4 w-full lg:w-6/12 xl:w-3/12 px-5">
    <div class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg">
        <div class="flex-auto p-4">
        <div class="flex flex-wrap">
            <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
            <h5 class="text-blueGray-400 uppercase font-bold text-xs">Sales</h5>
            <span class="font-semibold text-xl text-blueGray-700">901</span>
            </div>
            <div class="relative w-auto pl-4 flex-initial">
            <div class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full  bg-lightBlue-500">
                <i class="fas fa-users"></i>
            </div>
            </div>
        </div>
        <p class="text-sm text-blueGray-400 mt-4">
            <span class="text-red-500 mr-2"><i class="fas fa-arrow-down"></i> 1,25% </span>
            <span class="whitespace-nowrap"> Since yesterday </span></p>
        </div>
    </div>
    </div>

    <div class="mt-4 w-full lg:w-6/12 xl:w-3/12 px-5">
    <div class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg">
        <div class="flex-auto p-4">
        <div class="flex flex-wrap">
            <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
            <h5 class="text-blueGray-400 uppercase font-bold text-xs">Performance</h5>
            <span class="font-semibold text-xl text-blueGray-700">51.02% </span>
            </div>
            <div class="relative w-auto pl-4 flex-initial">
            <div class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full  bg-emerald-500">
                <i class="fas fa-percent"></i>
            </div>
            </div>
        </div>
        <p class="text-sm text-blueGray-400 mt-4">
            <span class="text-emerald-500 mr-2"><i class="fas fa-arrow-up"></i> 12% </span>
            <span class="whitespace-nowrap"> Since last mounth </span></p>
        </div>
    </div>
    </div>
</div>
<footer class="relative pt-8 pb-6">
  <div class="container mx-auto px-4">
    <div class="flex flex-wrap items-center md:justify-between justify-center">
      <div class="w-full md:w-6/12 px-4 mx-auto text-center">
        <div class="text-sm text-blueGray-500 font-semibold py-1">
          Made with <a href="https://www.creative-tim.com/product/notus-js" class="text-blueGray-500 hover:text-gray-800" target="_blank">Notus JS</a> by <a href="https://www.creative-tim.com" class="text-blueGray-500 hover:text-blueGray-800" target="_blank"> Creative Tim</a>.
        </div>
      </div>
    </div>
  </div>
</footer>'''
  },{
    "html":'''<div class="flex min-h-screen flex-row bg-gray-100 text-gray-800">
  <aside class="sidebar w-48 -translate-x-full transform bg-white p-4 transition-transform duration-150 ease-in md:translate-x-0 md:shadow-md">
    <div class="my-4 w-full border-b-4 border-indigo-100 text-center">
      <span class="font-mono text-xl font-bold tracking-widest"> <span class="text-indigo-600">HELLO</span> DEV </span>
    </div>
    <div class="my-4"></div>
  </aside>
  <main class="main -ml-48 flex flex-grow flex-col p-4 transition-all duration-150 ease-in md:ml-0">
    <div class="flex h-full items-center justify-center bg-white text-center text-5xl font-bold shadow-md">Content</div>
  </main>
</div>'''
},
{
    "html":'''<!-- full tailwind config using javascript -->
<!-- https://github.com/neurolinker/popice -->

<body class = "body bg-white dark:bg-[#0F172A]">
    <div class = "fixed w-full z-30 flex bg-white dark:bg-[#0F172A] p-2 items-center justify-center h-16 px-10">
        <div class = "logo ml-12 dark:text-white  transform ease-in-out duration-500 flex-none h-full flex items-center justify-center">
            NERVE
        </div>
        <!-- SPACER -->
        <div class = "grow h-full flex items-center justify-center"></div>
        <div class = "flex-none h-full text-center flex items-center justify-center">
            
                <div class = "flex space-x-3 items-center px-3">
                    <div class = "flex-none flex justify-center">
                    <div class="w-8 h-8 flex ">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShta_GXR2xdnsxSzj_GTcJHcNykjVKrCBrZ9qouUl0usuJWG2Rpr_PbTDu3sA9auNUH64&usqp=CAU" alt="profile" class="shadow rounded-full object-cover" />
                    </div>
                    </div>

                    <div class = "hidden md:block text-sm md:text-md text-black dark:text-white">John Doe</div>
                </div>
                
        </div>
    </div>
    <aside class = "w-60 -translate-x-48 fixed transition transform ease-in-out duration-1000 z-50 flex h-screen bg-[#1E293B] ">
        <!-- open sidebar button -->
        <div class = "max-toolbar translate-x-24 scale-x-0 w-full -right-6 transition transform ease-in duration-300 flex items-center justify-between border-4 border-white dark:border-[#0F172A] bg-[#1E293B]  absolute top-2 rounded-full h-12">
            
            <div class="flex pl-4 items-center space-x-2 ">
                <div>
                <div onclick="setDark('dark')" class="moon text-white hover:text-blue-500 dark:hover:text-[#38BDF8]">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={3} stroke="currentColor" class="w-4 h-4">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z" />
                    </svg>
                </div>
                <div onclick="setDark('light')" class = "sun hidden text-white hover:text-blue-500 dark:hover:text-[#38BDF8]">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
                      </svg>                      
                </div>
            </div >
                <div class = "text-white hover:text-blue-500 dark:hover:text-[#38BDF8]">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={3} stroke="currentColor" class="w-4 h-4">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
                    </svg>
                </div>
            </div>
            <div  class = "flex items-center space-x-3 group bg-gradient-to-r dark:from-cyan-500 dark:to-blue-500 from-indigo-500 via-purple-500 to-purple-500  pl-10 pr-2 py-1 rounded-full text-white  ">
                <div class= "transform ease-in-out duration-300 mr-12">
                    NERVE
                </div>
            </div>
        </div>
        <div onclick="openNav()" class = "-right-6 transition transform ease-in-out duration-500 flex border-4 border-white dark:border-[#0F172A] bg-[#1E293B] dark:hover:bg-blue-500 hover:bg-purple-500 absolute top-2 p-3 rounded-full text-white hover:rotate-45">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={3} stroke="currentColor" class="w-4 h-4">
                <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z" />
            </svg>
        </div>
        <!-- MAX SIDEBAR-->
        <div class= "max hidden text-white mt-20 flex-col space-y-2 w-full h-[calc(100vh)]">
            <div class =  "hover:ml-4 w-full text-white hover:text-purple-500 dark:hover:text-blue-500 bg-[#1E293B] p-2 pl-8 rounded-full transform ease-in-out duration-300 flex flex-row items-center space-x-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-4 h-4">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                </svg>    
                <div>
                    Home
                </div>
            </div>
            <div class =  "hover:ml-4 w-full text-white hover:text-purple-500 dark:hover:text-blue-500 bg-[#1E293B] p-2 pl-8 rounded-full transform ease-in-out duration-300 flex flex-row items-center space-x-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5" />
                </svg>                      
                <div>
                    Table
                </div>
            </div>
            <div class =  "hover:ml-4 w-full text-white hover:text-purple-500 dark:hover:text-blue-500 bg-[#1E293B] p-2 pl-8 rounded-full transform ease-in-out duration-300 flex flex-row items-center space-x-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6a7.5 7.5 0 107.5 7.5h-7.5V6z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0013.5 3v7.5z" />
                </svg>                      
                <div>
                    Graph
                </div>
            </div>
        </div>
        <!-- MINI SIDEBAR-->
        <div class= "mini mt-20 flex flex-col space-y-2 w-full h-[calc(100vh)]">
            <div class= "hover:ml-4 justify-end pr-5 text-white hover:text-purple-500 dark:hover:text-blue-500 w-full bg-[#1E293B] p-3 rounded-full transform ease-in-out duration-300 flex">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-4 h-4">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                </svg>                  
            </div>
            <div class= "hover:ml-4 justify-end pr-5 text-white hover:text-purple-500 dark:hover:text-blue-500 w-full bg-[#1E293B] p-3 rounded-full transform ease-in-out duration-300 flex">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5" />
                </svg>                 
            </div>
            <div class= "hover:ml-4 justify-end pr-5 text-white hover:text-purple-500 dark:hover:text-blue-500 w-full bg-[#1E293B] p-3 rounded-full transform ease-in-out duration-300 flex">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6a7.5 7.5 0 107.5 7.5h-7.5V6z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0013.5 3v7.5z" />
                </svg>           
            </div>
        </div>
        
    </aside>
    <!-- CONTENT -->
    <div class = "content ml-12 transform ease-in-out duration-500 pt-20 px-2 md:px-5 pb-4 ">
        <nav class = "flex px-5 py-3 text-gray-700  rounded-lg bg-gray-50 dark:bg-[#1E293B] " aria-label="Breadcrumb">
            <ol class = "inline-flex items-center space-x-1 md:space-x-3">
                <li class = "inline-flex items-center">
                    <a href="#" class = "inline-flex items-center text-sm font-medium text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white">
                        <svg class = "w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
                        Home
                    </a>
                </li>
                <li>
                    <div class = "flex items-center">
                        <svg class = "w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd"></path></svg>
                        <a href="#" class = "ml-1 text-sm font-medium text-gray-700 hover:text-gray-900 md:ml-2 dark:text-gray-400 dark:hover:text-white">Templates</a>
                    </div>
                </li>
            </ol>
        </nav>
        <div class = "flex flex-wrap my-5 -mx-2">
            <div class = "w-full lg:w-1/3 p-2">
                <div class = "flex items-center flex-row w-full bg-gradient-to-r dark:from-cyan-500 dark:to-blue-500 from-indigo-500 via-purple-500 to-pink-500 rounded-md p-3">
                    <div class = "flex text-indigo-500 dark:text-white items-center bg-white dark:bg-[#0F172A] p-2 rounded-md flex-none w-8 h-8 md:w-12 md:h-12 ">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class = "object-scale-down transition duration-500">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" />
                        </svg>
                    </div>
                    <div class = "flex flex-col justify-around flex-grow ml-5 text-white">
                        <div class = "text-xs whitespace-nowrap">
                            Total User
                        </div>
                        <div class = "">
                            100
                        </div>
                    </div>
                    <div class = " flex items-center flex-none text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class = "w-6 h-6">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                        </svg>

                    </div>
                </div>
            </div>
            <div class = "w-full md:w-1/2 lg:w-1/3 p-2 ">
                <div class = "flex items-center flex-row w-full bg-gradient-to-r dark:from-cyan-500 dark:to-blue-500 from-indigo-500 via-purple-500 to-pink-500 rounded-md p-3">
                    <div class = "flex text-indigo-500 dark:text-white items-center bg-white dark:bg-[#0F172A] p-2 rounded-md flex-none w-8 h-8 md:w-12 md:h-12 ">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class = "object-scale-down transition duration-500 ">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 18.75a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 01-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 00-3.213-9.193 2.056 2.056 0 00-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 00-10.026 0 1.106 1.106 0 00-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12" />
                        </svg>
                    </div>
                    <div class = "flex flex-col justify-around flex-grow ml-5 text-white">
                        <div class = "text-xs whitespace-nowrap">
                            Total Product
                        </div>
                        <div class = "">
                            500
                        </div>
                    </div>
                    <div class = " flex items-center flex-none text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class = "w-6 h-6">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                        </svg>

                    </div>
                </div>
            </div>
            <div class = "w-full md:w-1/2 lg:w-1/3 p-2">
                <div class = "flex items-center flex-row w-full bg-gradient-to-r dark:from-cyan-500 dark:to-blue-500 from-indigo-500 via-purple-500 to-pink-500 rounded-md p-3">
                    <div class = "flex text-indigo-500 dark:text-white items-center bg-white dark:bg-[#0F172A] p-2 rounded-md flex-none w-8 h-8 md:w-12 md:h-12 ">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class = "object-scale-down transition duration-500">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5m.75-9l3-3 2.148 2.148A12.061 12.061 0 0116.5 7.605" />
                    </svg>
                    </div>
                    <div class = "flex flex-col justify-around flex-grow ml-5 text-white">
                        <div class = "text-xs whitespace-nowrap">
                            Total Visitor
                        </div>
                        <div class = "">
                            500
                        </div>
                    </div>
                    <div class = " flex items-center flex-none text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class = "w-6 h-6">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                        </svg>

                    </div>
                </div>
            </div>
        </div>
        <div class = "p-4 mb-4 text-sm text-blue-700 bg-blue-100 rounded-lg dark:bg-blue-200 dark:text-blue-800" role="alert">
            <span class = "font-medium">Info alert!</span> Change a few things up and try submitting again.
        </div>
        <div class = "p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800" role="alert">
            <span class = "font-medium">Danger alert!</span> Change a few things up and try submitting again.
        </div>
        <div class = "p-4 mb-4 text-sm text-green-700 bg-green-100 rounded-lg dark:bg-green-200 dark:text-green-800" role="alert">
            <span class = "font-medium">Success alert!</span> Change a few things up and try submitting again.
        </div>
    </div>

    <script>
        const sidebar = document.querySelector("aside");
        const maxSidebar = document.querySelector(".max")
        const miniSidebar = document.querySelector(".mini")
        const roundout = document.querySelector(".roundout")
        const maxToolbar = document.querySelector(".max-toolbar")
        const logo = document.querySelector('.logo')
        const content = document.querySelector('.content')
        const moon = document.querySelector(".moon")
        const sun = document.querySelector(".sun")

        function setDark(val){
            if(val === "dark"){
                document.documentElement.classList.add('dark')
                moon.classList.add("hidden")
                sun.classList.remove("hidden")
            }else{
                document.documentElement.classList.remove('dark')
                sun.classList.add("hidden")
                moon.classList.remove("hidden")
            }
        }

        function openNav() {
            if(sidebar.classList.contains('-translate-x-48')){
                // max sidebar 
                sidebar.classList.remove("-translate-x-48")
                sidebar.classList.add("translate-x-none")
                maxSidebar.classList.remove("hidden")
                maxSidebar.classList.add("flex")
                miniSidebar.classList.remove("flex")
                miniSidebar.classList.add("hidden")
                maxToolbar.classList.add("translate-x-0")
                maxToolbar.classList.remove("translate-x-24","scale-x-0")
                logo.classList.remove("ml-12")
                content.classList.remove("ml-12")
                content.classList.add("ml-12","md:ml-60")
            }else{
                // mini sidebar
                sidebar.classList.add("-translate-x-48")
                sidebar.classList.remove("translate-x-none")
                maxSidebar.classList.add("hidden")
                maxSidebar.classList.remove("flex")
                miniSidebar.classList.add("flex")
                miniSidebar.classList.remove("hidden")
                maxToolbar.classList.add("translate-x-24","scale-x-0")
                maxToolbar.classList.remove("translate-x-0")
                logo.classList.add('ml-12')
                content.classList.remove("ml-12","md:ml-60")
                content.classList.add("ml-12")

            }

        }
    </script>'''
},{
    "html":'''<div class="w-full bg-white shadow-xl rounded-lg flex overflow-x-auto custom-scrollbar">
    <div class="w-64 px-4">
        <div class="h-16 flex items-center">
            <a href="#" class="w-48 mx-auto bg-blue-600 hover:bg-blue-700 flex items-center justify-center text-gray-100 py-2 rounded space-x-2 transition duration-150">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                </svg>
                <span>Compose</span>
            </a>
        </div>
        <div class="px-2 pt-4 pb-8 border-r border-gray-300">
            <ul class="space-y-2">
                <li>
                    <a class="bg-gray-500 bg-opacity-30 text-blue-600 flex items-center justify-between py-1.5 px-4 rounded cursor-pointer">
                        <span class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path>
                            </svg>
                            <span>Inbox</span>
                        </span>
                        <span class="bg-sky-500 text-gray-100 font-bold px-2 py-0.5 text-xs rounded-lg">3</span>
                    </a>
                </li>
                <li>
                    <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-600 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                        </svg>
                        <span>Starred</span>
                    </a>
                </li>
                <li>
                    <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-600 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                        </svg>
                        <span>Snoozed</span>
                    </a>
                </li>
                <li>
                    <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-600 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                        </svg>
                        <span>Important</span>
                    </a>
                </li>
                <li>
                    <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-600 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
                        </svg>
                        <span>Sent</span>
                    </a>
                </li>
                <li>
                    <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-600 flex items-center justify-between text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                        <span class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                            </svg>
                            <span>Drafts</span>
                        </span>
                        <span class="bg-sky-500 text-gray-100 font-bold px-2 py-0.5 text-xs rounded-lg">1</span>
                    </a>
                </li>
                <li>
                    <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-600 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                        </svg>
                        <span>Spam</span>
                    </a>
                </li>
                <li>
                    <a class="hover:bg-gray-500 hover:bg-opacity-10 hover:text-blue-600 flex items-center text-gray-700 py-1.5 px-4 rounded space-x-2 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                        </svg>
                        <span>Trash</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
    <div class="flex-1 px-2" x-data="{ checkAll: false, filterMessages: false }">
        <div class="h-16 flex items-center justify-between">
            <div class="flex items-center">
                <div class="relative flex items-center px-0.5 space-x-0.5">
                    <input @click="checkAll = !checkAll" type="checkbox" class="focus:ring-0">
                    <button @click="filterMessages = !filterMessages">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                        </svg>
                    </button>
                    <div x-show="filterMessages" @click.away="filterMessages = false" class="bg-gray-200 shadow-2xl absolute left-0 top-6 w-32 py-2 text-gray-900 rounded z-10" style="display: none;">
                        <button @click="filterMessages = false" class="w-full text-sm py-1 hover:bg-blue-600 hover:bg-opacity-30">
                            All
                        </button>
                        <button @click="filterMessages = false" class="w-full text-sm py-1 hover:bg-blue-600 hover:bg-opacity-30">
                            None
                        </button>
                        <button @click="filterMessages = false" class="w-full text-sm py-1 hover:bg-blue-600 hover:bg-opacity-30">
                            Read
                        </button>
                        <button @click="filterMessages = false" class="w-full text-sm py-1 hover:bg-blue-600 hover:bg-opacity-30">
                            Unread
                        </button>
                        <button @click="filterMessages = false" class="w-full text-sm py-1 hover:bg-blue-600 hover:bg-opacity-30">
                            Starred
                        </button>
                        <button @click="filterMessages = false" class="w-full text-sm py-1 hover:bg-blue-600 hover:bg-opacity-30">
                            Unstarred
                        </button>
                    </div>
                </div>
                <div class="flex items-center">
                    <div class="flex items-center ml-3">
                        <button title="Reload" class="text-gray-700 px-2 py-1 border border-gray-300 rounded-lg shadow hover:bg-gray-200 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
                            </svg>
                        </button>
                    </div>
                    <span class="bg-gray-300 h-6 w-[.5px] mx-3"></span>
                    <div class="flex items-center space-x-2">
                        <button title="Archive" class="text-gray-700 px-2 py-1 border border-gray-300 rounded-lg shadow hover:bg-gray-200 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                            </svg>
                        </button>
                        <button title="Mark As Spam" class="text-gray-700 px-2 py-1 border border-gray-300 rounded-lg shadow hover:bg-gray-200 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                            </svg>
                        </button>
                        <button title="Delete" class="text-gray-700 px-2 py-1 border border-gray-300 rounded-lg shadow hover:bg-gray-200 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                            </svg>
                        </button>
                    </div>
                    <span class="bg-gray-300 h-6 w-[.5px] mx-3"></span>
                    <div class="flex items-center space-x-2">
                        <button title="Mark As Read" class="text-gray-700 px-2 py-1 border border-gray-300 rounded-lg shadow hover:bg-gray-200 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 19v-8.93a2 2 0 01.89-1.664l7-4.666a2 2 0 012.22 0l7 4.666A2 2 0 0121 10.07V19M3 19a2 2 0 002 2h14a2 2 0 002-2M3 19l6.75-4.5M21 19l-6.75-4.5M3 10l6.75 4.5M21 10l-6.75 4.5m0 0l-1.14.76a2 2 0 01-2.22 0l-1.14-.76"></path>
                            </svg>
                        </button>
                        <button title="Mark As Unread" class="text-gray-700 px-2 py-1 border border-gray-300 rounded-lg shadow hover:bg-gray-200 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                            </svg>
                        </button>
                        <button title="Add Star" class="text-gray-700 px-2 py-1 border border-gray-300 rounded-lg shadow hover:bg-gray-200 transition duration-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
            <div class="px-2 flex items-center space-x-4">
                <span class="text-sm text-gray-500">1-15 of 1,323</span>
                <div class="flex items-center space-x-2">
                    <button class="bg-gray-200 text-gray-400 p-1.5 rounded-lg" title="Newer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                        </svg>
                    </button>
                    <button class="bg-gray-200 hover:bg-gray-300 text-gray-700 p-1.5 rounded-lg transition duration-150" title="Older">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <div class="bg-gray-100 mb-6">
            <ul>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">William Livingston</span>
                            <span class="w-64 truncate">Lorem ipsum dolor sit amet</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Sed ut perspiciatis unde omnis iste natus error sit voluptatem</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                3:05 PM
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-yellow-500 hover:text-yellow-600 h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 font-bold truncate">Betty Garmon</span>
                            <span class="w-64 font-bold truncate">Consectetur adipiscing elit</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Ccusantium doloremque laudantium, totam rem aperiam, eaque ipsa</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Read">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 19v-8.93a2 2 0 01.89-1.664l7-4.666a2 2 0 012.22 0l7 4.666A2 2 0 0121 10.07V19M3 19a2 2 0 002 2h14a2 2 0 002-2M3 19l6.75-4.5M21 19l-6.75-4.5M3 10l6.75 4.5M21 10l-6.75 4.5m0 0l-1.14.76a2 2 0 01-2.22 0l-1.14-.76"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm font-bold">
                                1:23 PM
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-yellow-500 hover:text-yellow-600 h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                                    </svg>
                                </button>
                                <button title="Email is marked as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-yellow-500 hover:text-yellow-600 h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                        <path d="M5 4a2 2 0 012-2h6a2 2 0 012 2v14l-5-2.5L5 18V4z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 font-bold truncate">Elsa J. Collins</span>
                            <span class="w-64 font-bold truncate">Sed do eiusmod tempor incididunt</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Read">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 19v-8.93a2 2 0 01.89-1.664l7-4.666a2 2 0 012.22 0l7 4.666A2 2 0 0121 10.07V19M3 19a2 2 0 002 2h14a2 2 0 002-2M3 19l6.75-4.5M21 19l-6.75-4.5M3 10l6.75 4.5M21 10l-6.75 4.5m0 0l-1.14.76a2 2 0 01-2.22 0l-1.14-.76"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm font-bold">
                                Jan 29
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Ellen Orozco</span>
                            <span class="w-64 truncate">Labore et dolore magna aliqua</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Nemo enim ipsam voluptatem quia voluptas sit</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 29
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Casey Jackson</span>
                            <span class="w-64 truncate">Ut enim ad minim veniam</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Aspernatur aut odit aut fugit, sed quia consequuntur</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 26
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 font-bold truncate">Jerry Brown</span>
                            <span class="w-64 font-bold truncate">Quis nostrud exercitation</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Magni dolores eos qui ratione voluptatem sequi nesciunt</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Read">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 19v-8.93a2 2 0 01.89-1.664l7-4.666a2 2 0 012.22 0l7 4.666A2 2 0 0121 10.07V19M3 19a2 2 0 002 2h14a2 2 0 002-2M3 19l6.75-4.5M21 19l-6.75-4.5M3 10l6.75 4.5M21 10l-6.75 4.5m0 0l-1.14.76a2 2 0 01-2.22 0l-1.14-.76"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm font-bold">
                                Jan 25
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Rob Brandt</span>
                            <span class="w-64 truncate">Ullamco laboris nisi ut aliquip</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Neque porro quisquam est, qui</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 25
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Edith Banks</span>
                            <span class="w-64 truncate">Commodo consequat</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Dolorem ipsum quia dolor sit amet, consectetur, adipisci velit</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 25
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Cindy Barth</span>
                            <span class="w-64 truncate">Duis aute irure dolor in reprehenderit</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Sed quia non numquam eius modi tempora incidunt ut</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500" style="">
                                Jan 25
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Debra Thomas</span>
                            <span class="w-64 truncate">Voluptate velit esse cillum</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Labore et dolore magnam aliquam quaerat voluptatem</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500" style="">
                                Jan 19
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Karen Jones</span>
                            <span class="w-64 truncate">Dolore eu fugiat nulla pariatur</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Ut enim ad minima veniam, quis nostrum exercitationem</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500" style="">
                                Jan 18
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Sonia Washington</span>
                            <span class="w-64 truncate">Excepteur sint occaecat</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 18
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Jonas Santana</span>
                            <span class="w-64 truncate">Cupidatat non proident</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Quis autem vel eum iure reprehenderit qui in ea voluptate</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 17
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Mary Barks</span>
                            <span class="w-64 truncate">Sunt in culpa qui officia</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Velit esse quam nihil molestiae consequatur</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 12
                            </span>
                        </div>
                    </div>
                </li>
                <li class="flex items-center border-y hover:bg-gray-200 px-2">
                    <input type="checkbox" class="focus:ring-0 border-2 border-gray-400" :checked="checkAll">
                    <div x-data="{ messageHover: false }" @mouseover="messageHover = true" @mouseleave="messageHover = false" class="w-full flex items-center justify-between p-1 my-1 cursor-pointer">
                        <div class="flex items-center">
                            <div class="flex items-center mr-4 ml-1 space-x-1">
                                <button title="Not starred">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
                                    </svg>
                                </button>
                                <button title="Click to mark this email as important">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span class="w-56 pr-2 truncate">Rachel Mullane</span>
                            <span class="w-64 truncate">Deserunt mollit anim id est laborum</span>
                            <span class="mx-1">-</span>
                            <span class="w-96 text-gray-600 text-sm truncate">Vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?</span>
                        </div>
                        <div class="w-32 flex items-center justify-end">
                            <div x-show="messageHover" class="flex items-center space-x-2" style="display: none;">
                                <button title="Archive">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-2m-4-1v8m0 0l3-3m-3 3L9 8m-5 5h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 00.707.293h3.172a1 1 0 00.707-.293l2.414-2.414a1 1 0 01.707-.293H20"></path>
                                    </svg>
                                </button>
                                <button title="Delete">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                                <button title="Mark As Unread">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                    </svg>
                                </button>
                                <button title="Snooze">    
                                    <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-gray-900 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </button>
                            </div>
                            <span x-show="!messageHover" class="text-sm text-gray-500">
                                Jan 10
                            </span>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>'''
},{
    "html":'''<!-- This is an example component -->
<div>
   <nav class="bg-white border-b border-gray-200 fixed z-30 w-full">
      <div class="px-3 py-3 lg:px-5 lg:pl-3">
         <div class="flex items-center justify-between">
            <div class="flex items-center justify-start">
               <button id="toggleSidebarMobile" aria-expanded="true" aria-controls="sidebar" class="lg:hidden mr-2 text-gray-600 hover:text-gray-900 cursor-pointer p-2 hover:bg-gray-100 focus:bg-gray-100 focus:ring-2 focus:ring-gray-100 rounded">
                  <svg id="toggleSidebarMobileHamburger" class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                     <path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h6a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path>
                  </svg>
                  <svg id="toggleSidebarMobileClose" class="w-6 h-6 hidden" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                     <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                  </svg>
               </button>
               <a href="#" class="text-xl font-bold flex items-center lg:ml-2.5">
               <img src="https://demo.themesberg.com/windster/images/logo.svg" class="h-6 mr-2" alt="Windster Logo">
               <span class="self-center whitespace-nowrap">Windster</span>
               </a>
               <form action="#" method="GET" class="hidden lg:block lg:pl-32">
                  <label for="topbar-search" class="sr-only">Search</label>
                  <div class="mt-1 relative lg:w-64">
                     <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                        <svg class="w-5 h-5 text-gray-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                           <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                        </svg>
                     </div>
                     <input type="text" name="email" id="topbar-search" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full pl-10 p-2.5" placeholder="Search">
                  </div>
               </form>
            </div>
            <div class="flex items-center">
               <button id="toggleSidebarMobileSearch" type="button" class="lg:hidden text-gray-500 hover:text-gray-900 hover:bg-gray-100 p-2 rounded-lg">
                  <span class="sr-only">Search</span>
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                     <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                  </svg>
               </button>
               <div class="hidden lg:flex items-center">
                  <span class="text-base font-normal text-gray-500 mr-5">Open source ❤️</span>
                  <div class="-mb-1">
                     <a class="github-button" href="#" data-color-scheme="no-preference: dark; light: light; dark: light;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star themesberg/windster-tailwind-css-dashboard on GitHub">Star</a>
                  </div>
               </div>
               <a href="#" class="hidden sm:inline-flex ml-5 text-white bg-cyan-600 hover:bg-cyan-700 focus:ring-4 focus:ring-cyan-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center items-center mr-3">
                  <svg class="svg-inline--fa fa-gem -ml-1 mr-2 h-4 w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="gem" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                     <path fill="currentColor" d="M378.7 32H133.3L256 182.7L378.7 32zM512 192l-107.4-141.3L289.6 192H512zM107.4 50.67L0 192h222.4L107.4 50.67zM244.3 474.9C247.3 478.2 251.6 480 256 480s8.653-1.828 11.67-5.062L510.6 224H1.365L244.3 474.9z"></path>
                  </svg>
                  Upgrade to Pro
               </a>
            </div>
         </div>
      </div>
   </nav>
   <div class="flex overflow-hidden bg-white pt-16">
      <aside id="sidebar" class="fixed hidden z-20 h-full top-0 left-0 pt-16 flex lg:flex flex-shrink-0 flex-col w-64 transition-width duration-75" aria-label="Sidebar">
         <div class="relative flex-1 flex flex-col min-h-0 border-r border-gray-200 bg-white pt-0">
            <div class="flex-1 flex flex-col pt-5 pb-4 overflow-y-auto">
               <div class="flex-1 px-3 bg-white divide-y space-y-1">
                  <ul class="space-y-2 pb-2">
                     <li>
                        <form action="#" method="GET" class="lg:hidden">
                           <label for="mobile-search" class="sr-only">Search</label>
                           <div class="relative">
                              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                 <svg class="w-5 h-5 text-gray-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>
                                 </svg>
                              </div>
                              <input type="text" name="email" id="mobile-search" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:ring-cyan-600 block w-full pl-10 p-2.5" placeholder="Search">
                           </div>
                        </form>
                     </li>
                     <li>
                        <a href="#" class="text-base text-gray-900 font-normal rounded-lg flex items-center p-2 hover:bg-gray-100 group">
                           <svg class="w-6 h-6 text-gray-500 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path>
                              <path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path>
                           </svg>
                           <span class="ml-3">Dashboard</span>
                        </a>
                     </li>
                     <li>
                        <a href="#" target="_blank" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 flex items-center p-2 group ">
                           <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>
                           </svg>
                           <span class="ml-3 flex-1 whitespace-nowrap">Kanban</span>
                           <span class="bg-gray-200 text-gray-800 ml-3 text-sm font-medium inline-flex items-center justify-center px-2 rounded-full">Pro</span>
                        </a>
                     </li>
                     <li>
                        <a href="#" target="_blank" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 flex items-center p-2 group ">
                           <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path d="M8.707 7.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l2-2a1 1 0 00-1.414-1.414L11 7.586V3a1 1 0 10-2 0v4.586l-.293-.293z"></path>
                              <path d="M3 5a2 2 0 012-2h1a1 1 0 010 2H5v7h2l1 2h4l1-2h2V5h-1a1 1 0 110-2h1a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z"></path>
                           </svg>
                           <span class="ml-3 flex-1 whitespace-nowrap">Inbox</span>
                           <span class="bg-gray-200 text-gray-800 ml-3 text-sm font-medium inline-flex items-center justify-center px-2 rounded-full">Pro</span>
                        </a>
                     </li>
                     <li>
                        <a href="#" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 flex items-center p-2 group ">
                           <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path>
                           </svg>
                           <span class="ml-3 flex-1 whitespace-nowrap">Users</span>
                        </a>
                     </li>
                     <li>
                        <a href="#" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 flex items-center p-2 group ">
                           <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z" clip-rule="evenodd"></path>
                           </svg>
                           <span class="ml-3 flex-1 whitespace-nowrap">Products</span>
                        </a>
                     </li>
                     <li>
                        <a href="#" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 flex items-center p-2 group ">
                           <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z" clip-rule="evenodd"></path>
                           </svg>
                           <span class="ml-3 flex-1 whitespace-nowrap">Sign In</span>
                        </a>
                     </li>
                     <li>
                        <a href="#" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 flex items-center p-2 group ">
                           <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M5 4a3 3 0 00-3 3v6a3 3 0 003 3h10a3 3 0 003-3V7a3 3 0 00-3-3H5zm-1 9v-1h5v2H5a1 1 0 01-1-1zm7 1h4a1 1 0 001-1v-1h-5v2zm0-4h5V8h-5v2zM9 8H4v2h5V8z" clip-rule="evenodd"></path>
                           </svg>
                           <span class="ml-3 flex-1 whitespace-nowrap">Sign Up</span>
                        </a>
                     </li>
                  </ul>
                  <div class="space-y-2 pt-2">
                     <a href="#" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 group transition duration-75 flex items-center p-2">
                        <svg class="w-5 h-5 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="gem" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                           <path fill="currentColor" d="M378.7 32H133.3L256 182.7L378.7 32zM512 192l-107.4-141.3L289.6 192H512zM107.4 50.67L0 192h222.4L107.4 50.67zM244.3 474.9C247.3 478.2 251.6 480 256 480s8.653-1.828 11.67-5.062L510.6 224H1.365L244.3 474.9z"></path>
                        </svg>
                        <span class="ml-4">Upgrade to Pro</span>
                     </a>
                     <a href="#" target="_blank" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 group transition duration-75 flex items-center p-2">
                        <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                           <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path>
                           <path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="ml-3">Documentation</span>
                     </a>
                     <a href="#" target="_blank" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 group transition duration-75 flex items-center p-2">
                        <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                           <path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z"></path>
                        </svg>
                        <span class="ml-3">Components</span>
                     </a>
                     <a href="#" target="_blank" class="text-base text-gray-900 font-normal rounded-lg hover:bg-gray-100 group transition duration-75 flex items-center p-2">
                        <svg class="w-6 h-6 text-gray-500 flex-shrink-0 group-hover:text-gray-900 transition duration-75" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                           <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-2 0c0 .993-.241 1.929-.668 2.754l-1.524-1.525a3.997 3.997 0 00.078-2.183l1.562-1.562C15.802 8.249 16 9.1 16 10zm-5.165 3.913l1.58 1.58A5.98 5.98 0 0110 16a5.976 5.976 0 01-2.516-.552l1.562-1.562a4.006 4.006 0 001.789.027zm-4.677-2.796a4.002 4.002 0 01-.041-2.08l-.08.08-1.53-1.533A5.98 5.98 0 004 10c0 .954.223 1.856.619 2.657l1.54-1.54zm1.088-6.45A5.974 5.974 0 0110 4c.954 0 1.856.223 2.657.619l-1.54 1.54a4.002 4.002 0 00-2.346.033L7.246 4.668zM12 10a2 2 0 11-4 0 2 2 0 014 0z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="ml-3">Help</span>
                     </a>
                  </div>
               </div>
            </div>
         </div>
      </aside>
      <div class="bg-gray-900 opacity-50 hidden fixed inset-0 z-10" id="sidebarBackdrop"></div>
      <div id="main-content" class="h-full w-full bg-gray-50 relative overflow-y-auto lg:ml-64">
         <main>
            <div class="pt-6 px-4">
               <div class="w-full grid grid-cols-1 xl:grid-cols-2 2xl:grid-cols-3 gap-4">
                  <div class="bg-white shadow rounded-lg p-4 sm:p-6 xl:p-8  2xl:col-span-2">
                     <div class="flex items-center justify-between mb-4">
                        <div class="flex-shrink-0">
                           <span class="text-2xl sm:text-3xl leading-none font-bold text-gray-900">$45,385</span>
                           <h3 class="text-base font-normal text-gray-500">Sales this week</h3>
                        </div>
                        <div class="flex items-center justify-end flex-1 text-green-500 text-base font-bold">
                           12.5%
                           <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                           </svg>
                        </div>
                     </div>
                     <div id="main-chart"></div>
                  </div>
                  <div class="bg-white shadow rounded-lg p-4 sm:p-6 xl:p-8 ">
                     <div class="mb-4 flex items-center justify-between">
                        <div>
                           <h3 class="text-xl font-bold text-gray-900 mb-2">Latest Transactions</h3>
                           <span class="text-base font-normal text-gray-500">This is a list of latest transactions</span>
                        </div>
                        <div class="flex-shrink-0">
                           <a href="#" class="text-sm font-medium text-cyan-600 hover:bg-gray-100 rounded-lg p-2">View all</a>
                        </div>
                     </div>
                     <div class="flex flex-col mt-8">
                        <div class="overflow-x-auto rounded-lg">
                           <div class="align-middle inline-block min-w-full">
                              <div class="shadow overflow-hidden sm:rounded-lg">
                                 <table class="min-w-full divide-y divide-gray-200">
                                    <thead class="bg-gray-50">
                                       <tr>
                                          <th scope="col" class="p-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                             Transaction
                                          </th>
                                          <th scope="col" class="p-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                             Date & Time
                                          </th>
                                          <th scope="col" class="p-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                             Amount
                                          </th>
                                       </tr>
                                    </thead>
                                    <tbody class="bg-white">
                                       <tr>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-900">
                                             Payment from <span class="font-semibold">Bonnie Green</span>
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-500">
                                             Apr 23 ,2021
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-semibold text-gray-900">
                                             $2300
                                          </td>
                                       </tr>
                                       <tr class="bg-gray-50">
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-900 rounded-lg rounded-left">
                                             Payment refund to <span class="font-semibold">#00910</span>
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-500">
                                             Apr 23 ,2021
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-semibold text-gray-900">
                                             -$670
                                          </td>
                                       </tr>
                                       <tr>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-900">
                                             Payment failed from <span class="font-semibold">#087651</span>
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-500">
                                             Apr 18 ,2021
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-semibold text-gray-900">
                                             $234
                                          </td>
                                       </tr>
                                       <tr class="bg-gray-50">
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-900 rounded-lg rounded-left">
                                             Payment from <span class="font-semibold">Lana Byrd</span>
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-500">
                                             Apr 15 ,2021
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-semibold text-gray-900">
                                             $5000
                                          </td>
                                       </tr>
                                       <tr>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-900">
                                             Payment from <span class="font-semibold">Jese Leos</span>
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-500">
                                             Apr 15 ,2021
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-semibold text-gray-900">
                                             $2300
                                          </td>
                                       </tr>
                                       <tr class="bg-gray-50">
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-900 rounded-lg rounded-left">
                                             Payment from <span class="font-semibold">THEMESBERG LLC</span>
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-500">
                                             Apr 11 ,2021
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-semibold text-gray-900">
                                             $560
                                          </td>
                                       </tr>
                                       <tr>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-900">
                                             Payment from <span class="font-semibold">Lana Lysle</span>
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-normal text-gray-500">
                                             Apr 6 ,2021
                                          </td>
                                          <td class="p-4 whitespace-nowrap text-sm font-semibold text-gray-900">
                                             $1437
                                          </td>
                                       </tr>
                                    </tbody>
                                 </table>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="mt-4 w-full grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                  <div class="bg-white shadow rounded-lg p-4 sm:p-6 xl:p-8 ">
                     <div class="flex items-center">
                        <div class="flex-shrink-0">
                           <span class="text-2xl sm:text-3xl leading-none font-bold text-gray-900">2,340</span>
                           <h3 class="text-base font-normal text-gray-500">New products this week</h3>
                        </div>
                        <div class="ml-5 w-0 flex items-center justify-end flex-1 text-green-500 text-base font-bold">
                           14.6%
                           <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                           </svg>
                        </div>
                     </div>
                  </div>
                  <div class="bg-white shadow rounded-lg p-4 sm:p-6 xl:p-8 ">
                     <div class="flex items-center">
                        <div class="flex-shrink-0">
                           <span class="text-2xl sm:text-3xl leading-none font-bold text-gray-900">5,355</span>
                           <h3 class="text-base font-normal text-gray-500">Visitors this week</h3>
                        </div>
                        <div class="ml-5 w-0 flex items-center justify-end flex-1 text-green-500 text-base font-bold">
                           32.9%
                           <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
                           </svg>
                        </div>
                     </div>
                  </div>
                  <div class="bg-white shadow rounded-lg p-4 sm:p-6 xl:p-8 ">
                     <div class="flex items-center">
                        <div class="flex-shrink-0">
                           <span class="text-2xl sm:text-3xl leading-none font-bold text-gray-900">385</span>
                           <h3 class="text-base font-normal text-gray-500">User signups this week</h3>
                        </div>
                        <div class="ml-5 w-0 flex items-center justify-end flex-1 text-red-500 text-base font-bold">
                           -2.7%
                           <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                           </svg>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="grid grid-cols-1 2xl:grid-cols-2 xl:gap-4 my-4">
                  <div class="bg-white shadow rounded-lg mb-4 p-4 sm:p-6 h-full">
                     <div class="flex items-center justify-between mb-4">
                        <h3 class="text-xl font-bold leading-none text-gray-900">Latest Customers</h3>
                        <a href="#" class="text-sm font-medium text-cyan-600 hover:bg-gray-100 rounded-lg inline-flex items-center p-2">
                        View all
                        </a>
                     </div>
                     <div class="flow-root">
                        <ul role="list" class="divide-y divide-gray-200">
                           <li class="py-3 sm:py-4">
                              <div class="flex items-center space-x-4">
                                 <div class="flex-shrink-0">
                                    <img class="h-8 w-8 rounded-full" src="https://demo.themesberg.com/windster/images/users/neil-sims.png" alt="Neil image">
                                 </div>
                                 <div class="flex-1 min-w-0">
                                    <p class="text-sm font-medium text-gray-900 truncate">
                                       Neil Sims
                                    </p>
                                    <p class="text-sm text-gray-500 truncate">
                                       <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="17727a767e7b57607e7973646372653974787a">[email&#160;protected]</a>
                                    </p>
                                 </div>
                                 <div class="inline-flex items-center text-base font-semibold text-gray-900">
                                    $320
                                 </div>
                              </div>
                           </li>
                           <li class="py-3 sm:py-4">
                              <div class="flex items-center space-x-4">
                                 <div class="flex-shrink-0">
                                    <img class="h-8 w-8 rounded-full" src="https://demo.themesberg.com/windster/images/users/bonnie-green.png" alt="Neil image">
                                 </div>
                                 <div class="flex-1 min-w-0">
                                    <p class="text-sm font-medium text-gray-900 truncate">
                                       Bonnie Green
                                    </p>
                                    <p class="text-sm text-gray-500 truncate">
                                       <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d4b1b9b5bdb894a3bdbab0a7a0b1a6fab7bbb9">[email&#160;protected]</a>
                                    </p>
                                 </div>
                                 <div class="inline-flex items-center text-base font-semibold text-gray-900">
                                    $3467
                                 </div>
                              </div>
                           </li>
                           <li class="py-3 sm:py-4">
                              <div class="flex items-center space-x-4">
                                 <div class="flex-shrink-0">
                                    <img class="h-8 w-8 rounded-full" src="https://demo.themesberg.com/windster/images/users/michael-gough.png" alt="Neil image">
                                 </div>
                                 <div class="flex-1 min-w-0">
                                    <p class="text-sm font-medium text-gray-900 truncate">
                                       Michael Gough
                                    </p>
                                    <p class="text-sm text-gray-500 truncate">
                                       <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="57323a363e3b17203e3933242332257934383a">[email&#160;protected]</a>
                                    </p>
                                 </div>
                                 <div class="inline-flex items-center text-base font-semibold text-gray-900">
                                    $67
                                 </div>
                              </div>
                           </li>
                           <li class="py-3 sm:py-4">
                              <div class="flex items-center space-x-4">
                                 <div class="flex-shrink-0">
                                    <img class="h-8 w-8 rounded-full" src="https://demo.themesberg.com/windster/images/users/thomas-lean.png" alt="Neil image">
                                 </div>
                                 <div class="flex-1 min-w-0">
                                    <p class="text-sm font-medium text-gray-900 truncate">
                                       Thomes Lean
                                    </p>
                                    <p class="text-sm text-gray-500 truncate">
                                       <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="284d45494144685f41464c5b5c4d5a064b4745">[email&#160;protected]</a>
                                    </p>
                                 </div>
                                 <div class="inline-flex items-center text-base font-semibold text-gray-900">
                                    $2367
                                 </div>
                              </div>
                           </li>
                           <li class="pt-3 sm:pt-4 pb-0">
                              <div class="flex items-center space-x-4">
                                 <div class="flex-shrink-0">
                                    <img class="h-8 w-8 rounded-full" src="https://demo.themesberg.com/windster/images/users/lana-byrd.png" alt="Neil image">
                                 </div>
                                 <div class="flex-1 min-w-0">
                                    <p class="text-sm font-medium text-gray-900 truncate">
                                       Lana Byrd
                                    </p>
                                    <p class="text-sm text-gray-500 truncate">
                                       <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="a2c7cfc3cbcee2d5cbccc6d1d6c7d08cc1cdcf">[email&#160;protected]</a>
                                    </p>
                                 </div>
                                 <div class="inline-flex items-center text-base font-semibold text-gray-900">
                                    $367
                                 </div>
                              </div>
                           </li>
                        </ul>
                     </div>
                  </div>
                  <div class="bg-white shadow rounded-lg p-4 sm:p-6 xl:p-8 ">
                     <h3 class="text-xl leading-none font-bold text-gray-900 mb-10">Acquisition Overview</h3>
                     <div class="block w-full overflow-x-auto">
                        <table class="items-center w-full bg-transparent border-collapse">
                           <thead>
                              <tr>
                                 <th class="px-4 bg-gray-50 text-gray-700 align-middle py-3 text-xs font-semibold text-left uppercase border-l-0 border-r-0 whitespace-nowrap">Top Channels</th>
                                 <th class="px-4 bg-gray-50 text-gray-700 align-middle py-3 text-xs font-semibold text-left uppercase border-l-0 border-r-0 whitespace-nowrap">Users</th>
                                 <th class="px-4 bg-gray-50 text-gray-700 align-middle py-3 text-xs font-semibold text-left uppercase border-l-0 border-r-0 whitespace-nowrap min-w-140-px"></th>
                              </tr>
                           </thead>
                           <tbody class="divide-y divide-gray-100">
                              <tr class="text-gray-500">
                                 <th class="border-t-0 px-4 align-middle text-sm font-normal whitespace-nowrap p-4 text-left">Organic Search</th>
                                 <td class="border-t-0 px-4 align-middle text-xs font-medium text-gray-900 whitespace-nowrap p-4">5,649</td>
                                 <td class="border-t-0 px-4 align-middle text-xs whitespace-nowrap p-4">
                                    <div class="flex items-center">
                                       <span class="mr-2 text-xs font-medium">30%</span>
                                       <div class="relative w-full">
                                          <div class="w-full bg-gray-200 rounded-sm h-2">
                                             <div class="bg-cyan-600 h-2 rounded-sm" style="width: 30%"></div>
                                          </div>
                                       </div>
                                    </div>
                                 </td>
                              </tr>
                              <tr class="text-gray-500">
                                 <th class="border-t-0 px-4 align-middle text-sm font-normal whitespace-nowrap p-4 text-left">Referral</th>
                                 <td class="border-t-0 px-4 align-middle text-xs font-medium text-gray-900 whitespace-nowrap p-4">4,025</td>
                                 <td class="border-t-0 px-4 align-middle text-xs whitespace-nowrap p-4">
                                    <div class="flex items-center">
                                       <span class="mr-2 text-xs font-medium">24%</span>
                                       <div class="relative w-full">
                                          <div class="w-full bg-gray-200 rounded-sm h-2">
                                             <div class="bg-orange-300 h-2 rounded-sm" style="width: 24%"></div>
                                          </div>
                                       </div>
                                    </div>
                                 </td>
                              </tr>
                              <tr class="text-gray-500">
                                 <th class="border-t-0 px-4 align-middle text-sm font-normal whitespace-nowrap p-4 text-left">Direct</th>
                                 <td class="border-t-0 px-4 align-middle text-xs font-medium text-gray-900 whitespace-nowrap p-4">3,105</td>
                                 <td class="border-t-0 px-4 align-middle text-xs whitespace-nowrap p-4">
                                    <div class="flex items-center">
                                       <span class="mr-2 text-xs font-medium">18%</span>
                                       <div class="relative w-full">
                                          <div class="w-full bg-gray-200 rounded-sm h-2">
                                             <div class="bg-teal-400 h-2 rounded-sm" style="width: 18%"></div>
                                          </div>
                                       </div>
                                    </div>
                                 </td>
                              </tr>
                              <tr class="text-gray-500">
                                 <th class="border-t-0 px-4 align-middle text-sm font-normal whitespace-nowrap p-4 text-left">Social</th>
                                 <td class="border-t-0 px-4 align-middle text-xs font-medium text-gray-900 whitespace-nowrap p-4">1251</td>
                                 <td class="border-t-0 px-4 align-middle text-xs whitespace-nowrap p-4">
                                    <div class="flex items-center">
                                       <span class="mr-2 text-xs font-medium">12%</span>
                                       <div class="relative w-full">
                                          <div class="w-full bg-gray-200 rounded-sm h-2">
                                             <div class="bg-pink-600 h-2 rounded-sm" style="width: 12%"></div>
                                          </div>
                                       </div>
                                    </div>
                                 </td>
                              </tr>
                              <tr class="text-gray-500">
                                 <th class="border-t-0 px-4 align-middle text-sm font-normal whitespace-nowrap p-4 text-left">Other</th>
                                 <td class="border-t-0 px-4 align-middle text-xs font-medium text-gray-900 whitespace-nowrap p-4">734</td>
                                 <td class="border-t-0 px-4 align-middle text-xs whitespace-nowrap p-4">
                                    <div class="flex items-center">
                                       <span class="mr-2 text-xs font-medium">9%</span>
                                       <div class="relative w-full">
                                          <div class="w-full bg-gray-200 rounded-sm h-2">
                                             <div class="bg-indigo-600 h-2 rounded-sm" style="width: 9%"></div>
                                          </div>
                                       </div>
                                    </div>
                                 </td>
                              </tr>
                              <tr class="text-gray-500">
                                 <th class="border-t-0 align-middle text-sm font-normal whitespace-nowrap p-4 pb-0 text-left">Email</th>
                                 <td class="border-t-0 align-middle text-xs font-medium text-gray-900 whitespace-nowrap p-4 pb-0">456</td>
                                 <td class="border-t-0 align-middle text-xs whitespace-nowrap p-4 pb-0">
                                    <div class="flex items-center">
                                       <span class="mr-2 text-xs font-medium">7%</span>
                                       <div class="relative w-full">
                                          <div class="w-full bg-gray-200 rounded-sm h-2">
                                             <div class="bg-purple-500 h-2 rounded-sm" style="width: 7%"></div>
                                          </div>
                                       </div>
                                    </div>
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                     </div>
                  </div>
               </div>
            </div>
         </main>
         <footer class="bg-white md:flex md:items-center md:justify-between shadow rounded-lg p-4 md:p-6 xl:p-8 my-6 mx-4">
            <ul class="flex items-center flex-wrap mb-6 md:mb-0">
               <li><a href="#" class="text-sm font-normal text-gray-500 hover:underline mr-4 md:mr-6">Terms and conditions</a></li>
               <li><a href="#" class="text-sm font-normal text-gray-500 hover:underline mr-4 md:mr-6">Privacy Policy</a></li>
               <li><a href="#" class="text-sm font-normal text-gray-500 hover:underline mr-4 md:mr-6">Licensing</a></li>
               <li><a href="#" class="text-sm font-normal text-gray-500 hover:underline mr-4 md:mr-6">Cookie Policy</a></li>
               <li><a href="#" class="text-sm font-normal text-gray-500 hover:underline">Contact</a></li>
            </ul>
            <div class="flex sm:justify-center space-x-6">
               <a href="#" class="text-gray-500 hover:text-gray-900">
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                     <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd" />
                  </svg>
               </a>
               <a href="#" class="text-gray-500 hover:text-gray-900">
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                     <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" />
                  </svg>
               </a>
               <a href="#" class="text-gray-500 hover:text-gray-900">
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                     <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
                  </svg>
               </a>
               <a href="#" class="text-gray-500 hover:text-gray-900">
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                     <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
                  </svg>
               </a>
               <a href="#" class="text-gray-500 hover:text-gray-900">
                  <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                     <path fill-rule="evenodd" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z" clip-rule="evenodd" />
                  </svg>
               </a>
            </div>
         </footer>
         <p class="text-center text-sm text-gray-500 my-10">
            &copy; 2019-2021 <a href="#" class="hover:underline" target="_blank">Themesberg</a>. All rights reserved.
         </p>
      </div>
   </div>
   <script async defer src="https://buttons.github.io/buttons.js"></script>
   <script src="https://demo.themesberg.com/windster/app.bundle.js"></script>
</div>'''
},{
    "html":'''<aside class="ml-[-100%] fixed z-10 top-0 pb-3 px-6 w-full flex flex-col justify-between h-screen border-r bg-white transition duration-300 md:w-4/12 lg:ml-0 lg:w-[25%] xl:w-[20%] 2xl:w-[15%]">
    <div>
        <div class="-mx-6 px-6 py-4">
            <a href="#" title="home">
                <img src="https://tailus.io/sources/blocks/stats-cards/preview/images/logo.svg" class="w-32" alt="tailus logo">
            </a>
        </div>

        <div class="mt-8 text-center">
            <img src="https://tailus.io/sources/blocks/stats-cards/preview/images/second_user.webp" alt="" class="w-10 h-10 m-auto rounded-full object-cover lg:w-28 lg:h-28">
            <h5 class="hidden mt-4 text-xl font-semibold text-gray-600 lg:block">Cynthia J. Watts</h5>
            <span class="hidden text-gray-400 lg:block">Admin</span>
        </div>

        <ul class="space-y-2 tracking-wide mt-8">
            <li>
                <a href="#" aria-label="dashboard" class="relative px-4 py-3 flex items-center space-x-4 rounded-xl text-white bg-gradient-to-r from-sky-600 to-cyan-400">
                    <svg class="-ml-1 h-6 w-6" viewBox="0 0 24 24" fill="none">
                        <path d="M6 8a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8ZM6 15a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-1Z" class="fill-current text-cyan-400 dark:fill-slate-600"></path>
                        <path d="M13 8a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2V8Z" class="fill-current text-cyan-200 group-hover:text-cyan-300"></path>
                        <path d="M13 15a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-1Z" class="fill-current group-hover:text-sky-300"></path>
                    </svg>
                    <span class="-mr-1 font-medium">Dashboard</span>
                </a>
            </li>
            <li>
                <a href="#" class="px-4 py-3 flex items-center space-x-4 rounded-md text-gray-600 group">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path class="fill-current text-gray-300 group-hover:text-cyan-300" fill-rule="evenodd" d="M2 6a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1H8a3 3 0 00-3 3v1.5a1.5 1.5 0 01-3 0V6z" clip-rule="evenodd" />
                        <path class="fill-current text-gray-600 group-hover:text-cyan-600" d="M6 12a2 2 0 012-2h8a2 2 0 012 2v2a2 2 0 01-2 2H2h2a2 2 0 002-2v-2z" />
                    </svg>
                    <span class="group-hover:text-gray-700">Categories</span>
                </a>
            </li>
            <li>
                <a href="#" class="px-4 py-3 flex items-center space-x-4 rounded-md text-gray-600 group">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path class="fill-current text-gray-600 group-hover:text-cyan-600" fill-rule="evenodd" d="M2 5a2 2 0 012-2h8a2 2 0 012 2v10a2 2 0 002 2H4a2 2 0 01-2-2V5zm3 1h6v4H5V6zm6 6H5v2h6v-2z" clip-rule="evenodd" />
                        <path class="fill-current text-gray-300 group-hover:text-cyan-300" d="M15 7h1a2 2 0 012 2v5.5a1.5 1.5 0 01-3 0V7z" />
                    </svg>
                    <span class="group-hover:text-gray-700">Reports</span>
                </a>
            </li>
            <li>
                <a href="#" class="px-4 py-3 flex items-center space-x-4 rounded-md text-gray-600 group">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path class="fill-current text-gray-600 group-hover:text-cyan-600" d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z" />
                        <path class="fill-current text-gray-300 group-hover:text-cyan-300" d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z" />
                    </svg>
                    <span class="group-hover:text-gray-700">Other data</span>
                </a>
            </li>
            <li>
                <a href="#" class="px-4 py-3 flex items-center space-x-4 rounded-md text-gray-600 group">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path class="fill-current text-gray-300 group-hover:text-cyan-300" d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z" />
                        <path class="fill-current text-gray-600 group-hover:text-cyan-600" fill-rule="evenodd" d="M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z" clip-rule="evenodd" />
                    </svg>
                    <span class="group-hover:text-gray-700">Finance</span>
                </a>
            </li>
        </ul>
    </div>

    <div class="px-6 -mx-6 pt-4 flex justify-between items-center border-t">
        <button class="px-4 py-3 flex items-center space-x-4 rounded-md text-gray-600 group">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
            <span class="group-hover:text-gray-700">Logout</span>
        </button>
    </div>
</aside>
<div class="ml-auto mb-6 lg:w-[75%] xl:w-[80%] 2xl:w-[85%]">
    <div class="sticky z-10 top-0 h-16 border-b bg-white lg:py-2.5">
        <div class="px-6 flex items-center justify-between space-x-4 2xl:container">
            <h5 hidden class="text-2xl text-gray-600 font-medium lg:block">Dashboard</h5>
            <button class="w-12 h-16 -mr-2 border-r lg:hidden">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 my-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
            </button>
            <div class="flex space-x-4">
                <!--search bar -->
                <div hidden class="md:block">
                    <div class="relative flex items-center text-gray-400 focus-within:text-cyan-400">
                        <span class="absolute left-4 h-6 flex items-center pr-3 border-r border-gray-300">
                        <svg xmlns="http://ww50w3.org/2000/svg" class="w-4 fill-current" viewBox="0 0 35.997 36.004">
                            <path id="Icon_awesome-search" data-name="search" d="M35.508,31.127l-7.01-7.01a1.686,1.686,0,0,0-1.2-.492H26.156a14.618,14.618,0,1,0-2.531,2.531V27.3a1.686,1.686,0,0,0,.492,1.2l7.01,7.01a1.681,1.681,0,0,0,2.384,0l1.99-1.99a1.7,1.7,0,0,0,.007-2.391Zm-20.883-7.5a9,9,0,1,1,9-9A8.995,8.995,0,0,1,14.625,23.625Z"></path>
                        </svg>
                        </span>
                        <input type="search" name="leadingIcon" id="leadingIcon" placeholder="Search here" class="w-full pl-14 pr-4 py-2.5 rounded-xl text-sm text-gray-600 outline-none border border-gray-300 focus:border-cyan-300 transition">
                    </div>
                </div>
                <!--/search bar -->
                <button aria-label="search" class="w-10 h-10 rounded-xl border bg-gray-100 focus:bg-gray-100 active:bg-gray-200 md:hidden">
                    <svg xmlns="http://ww50w3.org/2000/svg" class="w-4 mx-auto fill-current text-gray-600" viewBox="0 0 35.997 36.004">
                        <path id="Icon_awesome-search" data-name="search" d="M35.508,31.127l-7.01-7.01a1.686,1.686,0,0,0-1.2-.492H26.156a14.618,14.618,0,1,0-2.531,2.531V27.3a1.686,1.686,0,0,0,.492,1.2l7.01,7.01a1.681,1.681,0,0,0,2.384,0l1.99-1.99a1.7,1.7,0,0,0,.007-2.391Zm-20.883-7.5a9,9,0,1,1,9-9A8.995,8.995,0,0,1,14.625,23.625Z"></path>
                    </svg>
                </button>
                <button aria-label="chat" class="w-10 h-10 rounded-xl border bg-gray-100 focus:bg-gray-100 active:bg-gray-200">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 m-auto text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                    </svg>
                </button>
                <button aria-label="notification" class="w-10 h-10 rounded-xl border bg-gray-100 focus:bg-gray-100 active:bg-gray-200">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 m-auto text-gray-600" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z" />
                    </svg>
                </button>
            </div>
        </div>
    </div>

    <div class="px-6 pt-6 2xl:container">
        <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            <div class="md:col-span-2 lg:col-span-1" >
                <div class="h-full py-8 px-6 space-y-6 rounded-xl border border-gray-200 bg-white">
                    <svg class="w-40 m-auto opacity-75" viewBox="0 0 146 146" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M73.1866 5.7129C81.999 5.7129 90.725 7.44863 98.8666 10.821C107.008 14.1933 114.406 19.1363 120.637 25.3675C126.868 31.5988 131.811 38.9964 135.184 47.138C138.556 55.2796 140.292 64.0057 140.292 72.818C140.292 81.6304 138.556 90.3565 135.184 98.4981C131.811 106.64 126.868 114.037 120.637 120.269C114.406 126.5 107.008 131.443 98.8666 134.815C90.725 138.187 81.999 139.923 73.1866 139.923C64.3742 139.923 55.6481 138.187 47.5066 134.815C39.365 131.443 31.9674 126.5 25.7361 120.269C19.5048 114.037 14.5619 106.64 11.1895 98.4981C7.81717 90.3565 6.08144 81.6304 6.08144 72.818C6.08144 64.0057 7.81717 55.2796 11.1895 47.138C14.5619 38.9964 19.5048 31.5988 25.7361 25.3675C31.9674 19.1363 39.365 14.1933 47.5066 10.821C55.6481 7.44863 64.3742 5.7129 73.1866 5.7129L73.1866 5.7129Z" stroke="#e4e4f2" stroke-width="4.89873"/>
                        <path d="M73.5 23.4494C79.9414 23.4494 86.3198 24.7181 92.2709 27.1831C98.222 29.6482 103.629 33.2612 108.184 37.816C112.739 42.3707 116.352 47.778 118.817 53.7291C121.282 59.6802 122.551 66.0586 122.551 72.5C122.551 78.9414 121.282 85.3198 118.817 91.2709C116.352 97.222 112.739 102.629 108.184 107.184C103.629 111.739 98.222 115.352 92.2709 117.817C86.3198 120.282 79.9414 121.551 73.5 121.551C67.0586 121.551 60.6802 120.282 54.7291 117.817C48.778 115.352 43.3707 111.739 38.816 107.184C34.2612 102.629 30.6481 97.222 28.1831 91.2709C25.7181 85.3198 24.4494 78.9414 24.4494 72.5C24.4494 66.0586 25.7181 59.6802 28.1831 53.7291C30.6481 47.778 34.2612 42.3707 38.816 37.816C43.3707 33.2612 48.778 29.6481 54.7291 27.1831C60.6802 24.7181 67.0586 23.4494 73.5 23.4494L73.5 23.4494Z" stroke="#e4e4f2" stroke-width="4.89873"/>
                        <path d="M73 24C84.3364 24 95.3221 27.9307 104.085 35.1225C112.848 42.3142 118.847 52.322 121.058 63.4406C123.27 74.5592 121.558 86.1006 116.214 96.0984C110.87 106.096 102.225 113.932 91.7515 118.27C81.278 122.608 69.6243 123.181 58.7761 119.89C47.9278 116.599 38.5562 109.649 32.258 100.223C25.9598 90.7971 23.1248 79.479 24.2359 68.1972C25.3471 56.9153 30.3357 46.3678 38.3518 38.3518" stroke="url(#paint0_linear_622:13617)" stroke-width="10" stroke-linecap="round"/>
                        <path d="M73 5.00001C84.365 5.00001 95.5488 7.84852 105.529 13.2852C115.509 18.7218 123.968 26.5732 130.131 36.1217C136.295 45.6702 139.967 56.6112 140.812 67.9448C141.657 79.2783 139.648 90.6429 134.968 101C130.288 111.357 123.087 120.375 114.023 127.232C104.96 134.088 94.3218 138.563 83.0824 140.248C71.8431 141.933 60.3606 140.775 49.6845 136.878C39.0085 132.981 29.4793 126.471 21.9681 117.942" stroke="url(#paint1_linear_622:13617)" stroke-width="10" stroke-linecap="round"/>
                        <path d="M9.60279 97.5926C6.37325 89.2671 4.81515 80.3871 5.01745 71.4595C5.21975 62.5319 7.1785 53.7316 10.7818 45.561C14.3852 37.3904 19.5626 30.0095 26.0184 23.8398C32.4742 17.6701 40.082 12.8323 48.4075 9.6028" stroke="url(#paint2_linear_622:13617)" stroke-width="10" stroke-linecap="round"/>
                        <path d="M73 5.00001C86.6504 5.00001 99.9849 9.10831 111.269 16.7904" stroke="url(#paint3_linear_622:13617)" stroke-width="10" stroke-linecap="round"/>
                        <circle cx="73.5" cy="72.5" r="29" fill="#e4e4f2" stroke="#e4e4f2"/>
                        <path d="M74 82.8332C68.0167 82.8332 63.1666 77.9831 63.1666 71.9998C63.1666 66.0166 68.0167 61.1665 74 61.1665C79.9832 61.1665 84.8333 66.0166 84.8333 71.9998C84.8333 77.9831 79.9832 82.8332 74 82.8332ZM74 80.6665C76.2985 80.6665 78.5029 79.7534 80.1282 78.1281C81.7535 76.5028 82.6666 74.2984 82.6666 71.9998C82.6666 69.7013 81.7535 67.4969 80.1282 65.8716C78.5029 64.2463 76.2985 63.3332 74 63.3332C71.7014 63.3332 69.497 64.2463 67.8717 65.8716C66.2464 67.4969 65.3333 69.7013 65.3333 71.9998C65.3333 74.2984 66.2464 76.5028 67.8717 78.1281C69.497 79.7534 71.7014 80.6665 74 80.6665ZM70.75 67.6665H77.25L79.9583 71.4582L74 77.4165L68.0416 71.4582L70.75 67.6665ZM71.8658 69.8332L70.8691 71.2307L74 74.3615L77.1308 71.2307L76.1341 69.8332H71.8658Z" fill="#6A6A9F"/>
                        <defs>
                        <linearGradient id="paint0_linear_622:13617" x1="45.9997" y1="19" x2="46.0897" y2="124.308" gradientUnits="userSpaceOnUse">
                        <stop stop-color="#E323FF"/>
                        <stop offset="1" stop-color="#7517F8"/>
                        </linearGradient>
                        <linearGradient id="paint1_linear_622:13617" x1="1.74103e-06" y1="8.70228e-06" x2="6.34739e-08" y2="140.677" gradientUnits="userSpaceOnUse">
                        <stop stop-color="#4DFFDF"/>
                        <stop offset="1" stop-color="#4DA1FF"/>
                        </linearGradient>
                        <linearGradient id="paint2_linear_622:13617" x1="36.4997" y1="5.07257e-06" x2="36.6213" y2="142.36" gradientUnits="userSpaceOnUse">
                        <stop stop-color="#FFD422"/>
                        <stop offset="1" stop-color="#FF7D05"/>
                        </linearGradient>
                        <linearGradient id="paint3_linear_622:13617" x1="1.74103e-06" y1="8.70228e-06" x2="6.34739e-08" y2="140.677" gradientUnits="userSpaceOnUse">
                        <stop stop-color="#4DFFDF"/>
                        <stop offset="1" stop-color="#4DA1FF"/>
                        </linearGradient>
                        </defs>
                    </svg>
                    <div>
                        <h5 class="text-xl text-gray-600 text-center">Global Activities</h5>
                        <div class="mt-2 flex justify-center gap-4">
                            <h3 class="text-3xl font-bold text-gray-700">$23,988</h3>
                            <div class="flex items-end gap-1 text-green-500">
                                <svg class="w-3" viewBox="0 0 12 15" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M6.00001 0L12 8H-3.05176e-05L6.00001 0Z" fill="currentColor"/>
                                </svg>
                                <span>2%</span>
                            </div>
                        </div>
                        <span class="block text-center text-gray-500">Compared to last week $13,988</span>
                    </div>
                    <table class="w-full text-gray-600">
                        <tbody>
                            <tr>
                                <td class="py-2">Tailored ui</td>
                                <td class="text-gray-500">896</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 7C8.62687 7 7.61194 16 17.7612 16C27.9104 16 25.3731 9 34 9C42.6269 9 44.5157 5 51.2537 5C57.7936 5 59.3731 14.5 68 14.5" stroke="url(#paint0_linear_622:13631)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13631" x1="68" y1="7.74997" x2="1.69701" y2="8.10029" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#E323FF"/>
                                        <stop offset="1" stop-color="#7517F8"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                            <tr>
                                <td class="py-2">Customize</td>
                                <td class="text-gray-500">1200</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 12.929C8.69077 12.929 7.66833 9.47584 17.8928 9.47584C28.1172 9.47584 25.5611 15.9524 34.2519 15.9524C42.9426 15.9524 44.8455 10.929 51.6334 10.929C58.2217 10.929 59.3092 5 68 5" stroke="url(#paint0_linear_622:13640)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13640" x1="34" y1="5" x2="34" y2="15.9524" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#8AFF6C"/>
                                        <stop offset="1" stop-color="#02C751"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                            <tr>
                                <td class="py-2">Other</td>
                                <td class="text-gray-500">12</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 6C8.62687 6 6.85075 12.75 17 12.75C27.1493 12.75 25.3731 9 34 9C42.6269 9 42.262 13.875 49 13.875C55.5398 13.875 58.3731 6 67 6" stroke="url(#paint0_linear_622:13649)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13649" x1="67" y1="7.96873" x2="1.67368" y2="8.44377" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#FFD422"/>
                                        <stop offset="1" stop-color="#FF7D05"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                        </tbody>
                    </table> 
                </div>
            </div>
            <div>
                <div class="h-full py-6 px-6 rounded-xl border border-gray-200 bg-white">
                    <h5 class="text-xl text-gray-700">Downloads</h5>
                    <div class="my-8">
                        <h1 class="text-5xl font-bold text-gray-800">64,5%</h1>
                        <span class="text-gray-500">Compared to last week $13,988</span>
                    </div>
                    <svg class="w-full" viewBox="0 0 218 69" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M0 67.5C27.8998 67.5 24.6002 15 52.5 15C80.3998 15 77.1002 29 105 29C132.9 29 128.6 52 156.5 52C184.4 52 189.127 63.8158 217.027 63.8158" stroke="url(#paint0_linear_622:13664)" stroke-width="3" stroke-linecap="round"/>
                        <path d="M0 67.5C27.2601 67.5 30.7399 31 58 31C85.2601 31 80.7399 2 108 2C135.26 2 134.74 43 162 43C189.26 43 190.74 63.665 218 63.665" stroke="url(#paint1_linear_622:13664)" stroke-width="3" stroke-linecap="round"/>
                        <defs>
                        <linearGradient id="paint0_linear_622:13664" x1="217.027" y1="15" x2="7.91244" y2="15" gradientUnits="userSpaceOnUse">
                        <stop stop-color="#4DFFDF"/>
                        <stop offset="1" stop-color="#4DA1FF"/>
                        </linearGradient>
                        <linearGradient id="paint1_linear_622:13664" x1="218" y1="18.3748" x2="5.4362" y2="18.9795" gradientUnits="userSpaceOnUse">
                        <stop stop-color="#E323FF"/>
                        <stop offset="1" stop-color="#7517F8"/>
                        </linearGradient>
                        </defs>
                    </svg>
                    <table class="mt-6 -mb-2 w-full text-gray-600">
                        <tbody>
                            <tr>
                                <td class="py-2">From new users</td>
                                <td class="text-gray-500">896</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 7C8.62687 7 7.61194 16 17.7612 16C27.9104 16 25.3731 9 34 9C42.6269 9 44.5157 5 51.2537 5C57.7936 5 59.3731 14.5 68 14.5" stroke="url(#paint0_linear_622:13631)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13631" x1="68" y1="7.74997" x2="1.69701" y2="8.10029" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#E323FF"/>
                                        <stop offset="1" stop-color="#7517F8"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                            <tr>
                                <td class="py-2">From old users</td>
                                <td class="text-gray-500">1200</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 12.929C8.69077 12.929 7.66833 9.47584 17.8928 9.47584C28.1172 9.47584 25.5611 15.9524 34.2519 15.9524C42.9426 15.9524 44.8455 10.929 51.6334 10.929C58.2217 10.929 59.3092 5 68 5" stroke="url(#paint0_linear_622:13640)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13640" x1="34" y1="5" x2="34" y2="15.9524" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#8AFF6C"/>
                                        <stop offset="1" stop-color="#02C751"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                        </tbody>
                    </table>   
                </div>
            </div>
            <div>
                <div class="lg:h-full py-8 px-6 text-gray-600 rounded-xl border border-gray-200 bg-white">
                    <svg class="w-40 m-auto" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M27.9985 2.84071C31.2849 2.84071 34.539 3.488 37.5752 4.74562C40.6113 6.00324 43.3701 7.84657 45.6938 10.1703C48.0176 12.4941 49.861 15.2529 51.1186 18.289C52.3762 21.3252 53.0235 24.5793 53.0235 27.8657C53.0235 31.152 52.3762 34.4061 51.1186 37.4423C49.861 40.4785 48.0176 43.2372 45.6938 45.561C43.3701 47.8848 40.6113 49.7281 37.5752 50.9857C34.539 52.2433 31.2849 52.8906 27.9985 52.8906C24.7122 52.8906 21.4581 52.2433 18.4219 50.9857C15.3857 49.7281 12.627 47.8848 10.3032 45.561C7.97943 43.2372 6.1361 40.4785 4.87848 37.4423C3.62086 34.4061 2.97357 31.152 2.97357 27.8657C2.97357 24.5793 3.62086 21.3252 4.87848 18.289C6.13611 15.2529 7.97943 12.4941 10.3032 10.1703C12.627 7.84656 15.3857 6.00324 18.4219 4.74562C21.4581 3.488 24.7122 2.84071 27.9985 2.84071L27.9985 2.84071Z" stroke="#e4e4f2" stroke-width="3"/>
                        <path d="M27.301 2.50958C33.0386 2.35225 38.6614 4.13522 43.26 7.57004C47.8585 11.0049 51.1637 15.8907 52.641 21.437C54.1182 26.9834 53.6811 32.8659 51.4002 38.133C49.1194 43.4001 45.1283 47.7437 40.0726 50.4611C35.0169 53.1785 29.1923 54.1108 23.541 53.1071C17.8897 52.1034 12.7423 49.2225 8.93145 44.9305C5.12062 40.6384 2.86926 35.1861 2.54159 29.4558C2.21391 23.7254 3.82909 18.0521 7.12582 13.3536" stroke="url(#paint0_linear_622:13696)" stroke-width="5" stroke-linecap="round"/>
                        <path d="M13.3279 30.7467C13.3912 29.48 13.8346 28.5047 14.6579 27.8207C15.4939 27.124 16.5896 26.7757 17.9449 26.7757C18.8696 26.7757 19.6612 26.9404 20.3199 27.2697C20.9786 27.5864 21.4726 28.0234 21.8019 28.5807C22.1439 29.1254 22.3149 29.746 22.3149 30.4427C22.3149 31.2407 22.1059 31.9184 21.6879 32.4757C21.2826 33.0204 20.7949 33.3877 20.2249 33.5777V33.6537C20.9596 33.8817 21.5296 34.287 21.9349 34.8697C22.3529 35.4524 22.5619 36.1997 22.5619 37.1117C22.5619 37.8717 22.3846 38.5494 22.0299 39.1447C21.6879 39.74 21.1749 40.2087 20.4909 40.5507C19.8196 40.88 19.0089 41.0447 18.0589 41.0447C16.6276 41.0447 15.4622 40.6837 14.5629 39.9617C13.6636 39.2397 13.1886 38.1757 13.1379 36.7697H15.7219C15.7472 37.3904 15.9562 37.8907 16.3489 38.2707C16.7542 38.638 17.3052 38.8217 18.0019 38.8217C18.6479 38.8217 19.1419 38.6444 19.4839 38.2897C19.8386 37.9224 20.0159 37.4537 20.0159 36.8837C20.0159 36.1237 19.7752 35.579 19.2939 35.2497C18.8126 34.9204 18.0652 34.7557 17.0519 34.7557H16.5009V32.5707H17.0519C18.8506 32.5707 19.7499 31.969 19.7499 30.7657C19.7499 30.221 19.5852 29.7967 19.2559 29.4927C18.9392 29.1887 18.4769 29.0367 17.8689 29.0367C17.2736 29.0367 16.8112 29.2014 16.4819 29.5307C16.1652 29.8474 15.9816 30.2527 15.9309 30.7467H13.3279ZM25.6499 37.9477C26.8659 36.9344 27.8349 36.092 28.5569 35.4207C29.2789 34.7367 29.8806 34.0274 30.3619 33.2927C30.8433 32.558 31.0839 31.836 31.0839 31.1267C31.0839 30.4807 30.9319 29.974 30.6279 29.6067C30.3239 29.2394 29.8553 29.0557 29.2219 29.0557C28.5886 29.0557 28.1009 29.271 27.7589 29.7017C27.4169 30.1197 27.2396 30.696 27.2269 31.4307H24.6429C24.6936 29.9107 25.1433 28.758 25.9919 27.9727C26.8533 27.1874 27.9426 26.7947 29.2599 26.7947C30.7039 26.7947 31.8123 27.181 32.5849 27.9537C33.3576 28.7137 33.7439 29.7207 33.7439 30.9747C33.7439 31.9627 33.4779 32.9064 32.9459 33.8057C32.4139 34.705 31.8059 35.4904 31.1219 36.1617C30.4379 36.8204 29.5449 37.6184 28.4429 38.5557H34.0479V40.7597H24.6619V38.7837L25.6499 37.9477Z" fill="currentColor"/>
                        <path d="M36.1948 28.8842C36.1948 29.4438 36.2557 29.8634 36.3775 30.1432C36.4992 30.423 36.6967 30.5628 36.9699 30.5628C37.5097 30.5628 37.7796 30.0033 37.7796 28.8842C37.7796 27.7717 37.5097 27.2155 36.9699 27.2155C36.6967 27.2155 36.4992 27.3537 36.3775 27.6302C36.2557 27.9067 36.1948 28.3247 36.1948 28.8842ZM38.456 28.8842C38.456 29.6347 38.3293 30.2024 38.0758 30.5875C37.8257 30.9693 37.457 31.1602 36.9699 31.1602C36.5091 31.1602 36.1504 30.9644 35.8936 30.5727C35.6402 30.181 35.5135 29.6182 35.5135 28.8842C35.5135 28.1371 35.6352 27.5742 35.8788 27.1957C36.1257 26.8172 36.4894 26.6279 36.9699 26.6279C37.4472 26.6279 37.8142 26.8238 38.0709 27.2155C38.3276 27.6071 38.456 28.1634 38.456 28.8842ZM40.5395 31.7774C40.5395 32.3402 40.6003 32.7615 40.7221 33.0413C40.8439 33.3178 41.043 33.456 41.3195 33.456C41.596 33.456 41.8001 33.3194 41.9317 33.0462C42.0634 32.7697 42.1292 32.3468 42.1292 31.7774C42.1292 31.2145 42.0634 30.7982 41.9317 30.5283C41.8001 30.2551 41.596 30.1185 41.3195 30.1185C41.043 30.1185 40.8439 30.2551 40.7221 30.5283C40.6003 30.7982 40.5395 31.2145 40.5395 31.7774ZM42.8056 31.7774C42.8056 32.5245 42.6789 33.0906 42.4254 33.4757C42.1753 33.8575 41.8067 34.0484 41.3195 34.0484C40.8521 34.0484 40.4917 33.8526 40.2383 33.4609C39.9881 33.0693 39.8631 32.5081 39.8631 31.7774C39.8631 31.0302 39.9849 30.4674 40.2284 30.0889C40.4753 29.7104 40.839 29.5211 41.3195 29.5211C41.7869 29.5211 42.1506 29.7153 42.4106 30.1037C42.6739 30.4888 42.8056 31.0467 42.8056 31.7774ZM41.5318 26.7316L37.5278 33.9497H36.8021L40.8061 26.7316H41.5318Z" fill="white"/>
                        <path d="M23.5776 18.4198H25.5424V22.8407H23.5776V18.4198ZM30.4545 16.455H32.4193V22.8407H30.4545V16.455ZM27.0161 13.5078H28.9809V22.8407H27.0161V13.5078Z" fill="#6A6A9F"/>
                        <defs>
                        <linearGradient id="paint0_linear_622:13696" x1="5.54791e-07" y1="42.0001" x2="54.6039" y2="41.9535" gradientUnits="userSpaceOnUse">
                        <stop stop-color="#E323FF"/>
                        <stop offset="1" stop-color="#7517F8"/>
                        </linearGradient>
                        </defs>
                    </svg>
                    <div class="mt-6">
                        <h5 class="text-xl text-gray-700 text-center">Ask to customize</h5>
                        <div class="mt-2 flex justify-center gap-4">
                            <h3 class="text-3xl font-bold text-gray-700">28</h3>
                            <div class="flex items-end gap-1 text-green-500">
                                <svg class="w-3" viewBox="0 0 12 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M6.00001 0L12 8H-3.05176e-05L6.00001 0Z" fill="currentColor"/>
                                </svg>
                                <span>2%</span>
                            </div>
                        </div>
                        <span class="block text-center text-gray-500">Compared to last week 13</span>
                    </div>
                    <table class="mt-6 -mb-2 w-full text-gray-600">
                        <tbody>
                            <tr>
                                <td class="py-2">Tailored ui</td>
                                <td class="text-gray-500">896</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 7C8.62687 7 7.61194 16 17.7612 16C27.9104 16 25.3731 9 34 9C42.6269 9 44.5157 5 51.2537 5C57.7936 5 59.3731 14.5 68 14.5" stroke="url(#paint0_linear_622:13631)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13631" x1="68" y1="7.74997" x2="1.69701" y2="8.10029" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#E323FF"/>
                                        <stop offset="1" stop-color="#7517F8"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                            <tr>
                                <td class="py-2">Customize</td>
                                <td class="text-gray-500">1200</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 12.929C8.69077 12.929 7.66833 9.47584 17.8928 9.47584C28.1172 9.47584 25.5611 15.9524 34.2519 15.9524C42.9426 15.9524 44.8455 10.929 51.6334 10.929C58.2217 10.929 59.3092 5 68 5" stroke="url(#paint0_linear_622:13640)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13640" x1="34" y1="5" x2="34" y2="15.9524" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#8AFF6C"/>
                                        <stop offset="1" stop-color="#02C751"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                            <tr>
                                <td class="py-2">Other</td>
                                <td class="text-gray-500">12</td>
                                <td>
                                    <svg class="w-16 ml-auto" viewBox="0 0 68 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.4" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="19" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="35" width="14" height="21" rx="1" fill="#e4e4f2"/>
                                        <rect opacity="0.4" x="51" width="17" height="21" rx="1" fill="#e4e4f2"/>
                                        <path d="M0 6C8.62687 6 6.85075 12.75 17 12.75C27.1493 12.75 25.3731 9 34 9C42.6269 9 42.262 13.875 49 13.875C55.5398 13.875 58.3731 6 67 6" stroke="url(#paint0_linear_622:13649)" stroke-width="2" stroke-linejoin="round"/>
                                        <defs>
                                        <linearGradient id="paint0_linear_622:13649" x1="67" y1="7.96873" x2="1.67368" y2="8.44377" gradientUnits="userSpaceOnUse">
                                        <stop stop-color="#FFD422"/>
                                        <stop offset="1" stop-color="#FF7D05"/>
                                        </linearGradient>
                                        </defs>
                                    </svg>
                                </td>   
                            </tr>
                        </tbody>
                    </table>   
                </div>
            </div>
        </div>
    </div>
</div>'''
},{
    "html":'''<body class="font-poppins antialiased">
    <div
      id="view"
      class="h-full w-screen flex flex-row"
      x-data="{ sidenav: true }"
    >
      <button
        @click="sidenav = true"
        class="p-2 border-2 bg-white rounded-md border-gray-200 shadow-lg text-gray-500 focus:bg-teal-500 focus:outline-none focus:text-white absolute top-0 left-0 sm:hidden"
      >
        <svg
          class="w-5 h-5 fill-current"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </button>
      <div
        id="sidebar"
        class="bg-white h-screen md:block shadow-xl px-3 w-30 md:w-60 lg:w-60 overflow-x-hidden transition-transform duration-300 ease-in-out"
        x-show="sidenav"
        @click.away="sidenav = false"
      >
        <div class="space-y-6 md:space-y-10 mt-10">
          <h1 class="font-bold text-4xl text-center md:hidden">
            D<span class="text-teal-600">.</span>
          </h1>
          <h1 class="hidden md:block font-bold text-sm md:text-xl text-center">
            Dashwind<span class="text-teal-600">.</span>
          </h1>
          <div id="profile" class="space-y-3">
            <img
              src="https://images.unsplash.com/photo-1628157588553-5eeea00af15c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"
              alt="Avatar user"
              class="w-10 md:w-16 rounded-full mx-auto"
            />
            <div>
              <h2
                class="font-medium text-xs md:text-sm text-center text-teal-500"
              >
                Eduard Pantazi
              </h2>
              <p class="text-xs text-gray-500 text-center">Administrator</p>
            </div>
          </div>
          <div
            class="flex border-2 border-gray-200 rounded-md focus-within:ring-2 ring-teal-500"
          >
            <input
              type="text"
              class="w-full rounded-tl-md rounded-bl-md px-2 py-3 text-sm text-gray-600 focus:outline-none"
              placeholder="Search"
            />
            <button
              class="rounded-tr-md rounded-br-md px-2 py-3 hidden md:block"
            >
              <svg
                class="w-4 h-4 fill-current"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </button>
          </div>
          <div id="menu" class="flex flex-col space-y-2">
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:text-base rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
                ></path>
              </svg>
              <span class="">Dashboard</span>
            </a>
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:scale-105 rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M11 17a1 1 0 001.447.894l4-2A1 1 0 0017 15V9.236a1 1 0 00-1.447-.894l-4 2a1 1 0 00-.553.894V17zM15.211 6.276a1 1 0 000-1.788l-4.764-2.382a1 1 0 00-.894 0L4.789 4.488a1 1 0 000 1.788l4.764 2.382a1 1 0 00.894 0l4.764-2.382zM4.447 8.342A1 1 0 003 9.236V15a1 1 0 00.553.894l4 2A1 1 0 009 17v-5.764a1 1 0 00-.553-.894l-4-2z"
                ></path>
              </svg>
              <span class="">Products</span>
            </a>
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:scale-105 rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path>
                <path
                  fill-rule="evenodd"
                  d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="">Reports</span>
            </a>
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:scale-105 rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"
                ></path>
                <path
                  d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z"
                ></path>
              </svg>
              <span class="">Messages</span>
            </a>
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:scale-105 rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="">Calendar</span>
            </a>
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:scale-105 rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M3 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span class="">Table</span>
            </a>
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:scale-105 rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM14 11a1 1 0 011 1v1h1a1 1 0 110 2h-1v1a1 1 0 11-2 0v-1h-1a1 1 0 110-2h1v-1a1 1 0 011-1z"
                ></path>
              </svg>
              <span class="">UI Components</span>
            </a>
            <a
              href=""
              class="text-sm font-medium text-gray-700 py-2 px-2 hover:bg-teal-500 hover:text-white hover:scale-105 rounded-md transition duration-150 ease-in-out"
            >
              <svg
                class="w-6 h-6 fill-current inline-block"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"
                ></path>
              </svg>
              <span class="">Users</span>
            </a>
          </div>
        </div>
      </div>
     
    </div>
  </body>'''
}
]
Navigations =[
    {
    "html":'''<link rel="preconnect" href="https://rsms.me/">
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
<style>
    :root { font-family: 'Inter', sans-serif; }
@supports (font-variation-settings: normal) {
  :root { font-family: 'Inter var', sans-serif; }
}
</style>
<div class="bg-slate-100 overflow-y-scroll w-screen h-screen antialiased text-slate-300 selection:bg-blue-600 selection:text-white">
    <div class="flex flex-col relative w-screen">
        <div id="menu" class="bg-gray-900 min-h-screen z-10 text-slate-300 w-64 fixed left-0 h-screen overflow-y-scroll">
           <div id="logo" class="my-4 px-6">
            <h1 class="text-lg md:text-2xl font-bold text-white">Dash<span class="text-blue-500">8</span>.</h1>
            <p class="text-slate-500 text-sm">Manage your actions and activities</p>
           </div>
           <div id="profile" class="px-6 py-10">
            <p class="text-slate-500">Welcome back,</p>
            <a href="#" class="inline-flex space-x-2 items-center">
                <span>
                    <img class="rounded-full w-8 h-8" src="https://images.unsplash.com/photo-1542909168-82c3e7fdca5c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=128&q=80" alt="">
                </span>
                <span class="text-sm md:text-base font-bold">
                    Edward Tompson
                </span>
                </a>
           </div>
           <div id="nav" class="w-full px-6">
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 bg-blue-800 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-white">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z" />
                      </svg>
                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg font-bold leading-5 text-white">Dashboard</span>
                    <span class="text-sm text-white/50 hidden md:block">Data Overview</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" />
                      </svg>                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Database</span>
                    <span class="text-sm text-slate-500 hidden md:block">Database Manager</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15a4.5 4.5 0 004.5 4.5H18a3.75 3.75 0 001.332-7.257 3 3 0 00-3.758-3.848 5.25 5.25 0 00-10.233 2.33A4.502 4.502 0 002.25 15z" />
                      </svg>                        
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Cloud Storage</span>
                    <span class="text-sm text-slate-500 hidden md:block">Manage Cloud Storage</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3 3v1.5M3 21v-6m0 0l2.77-.693a9 9 0 016.208.682l.108.054a9 9 0 006.086.71l3.114-.732a48.524 48.524 0 01-.005-10.499l-3.11.732a9 9 0 01-6.085-.711l-.108-.054a9 9 0 00-6.208-.682L3 4.5M3 15V4.5" />
                      </svg>                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Reports</span>
                    <span class="text-sm text-slate-500 hidden md:block">Manage Reports</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" />
                      </svg>                      
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Security</span>
                    <span class="text-sm text-slate-500 hidden md:block">Generate Security Keys</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center border-b border-slate-700 py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 7.125C2.25 6.504 2.754 6 3.375 6h6c.621 0 1.125.504 1.125 1.125v3.75c0 .621-.504 1.125-1.125 1.125h-6a1.125 1.125 0 01-1.125-1.125v-3.75zM14.25 8.625c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v8.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-8.25zM3.75 16.125c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-2.25z" />
                      </svg>                                          
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Extensions</span>
                    <span class="text-sm text-slate-500 hidden md:block">Manage Extensions</span>
                </div>
            </a>
            <a href="#" class="w-full px-2 inline-flex space-x-2 items-center py-3 hover:bg-white/5 transition ease-linear duration-150">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12a7.5 7.5 0 0015 0m-15 0a7.5 7.5 0 1115 0m-15 0H3m16.5 0H21m-1.5 0H12m-8.457 3.077l1.41-.513m14.095-5.13l1.41-.513M5.106 17.785l1.15-.964m11.49-9.642l1.149-.964M7.501 19.795l.75-1.3m7.5-12.99l.75-1.3m-6.063 16.658l.26-1.477m2.605-14.772l.26-1.477m0 17.726l-.26-1.477M10.698 4.614l-.26-1.477M16.5 19.794l-.75-1.299M7.5 4.205L12 12m6.894 5.785l-1.149-.964M6.256 7.178l-1.15-.964m15.352 8.864l-1.41-.513M4.954 9.435l-1.41-.514M12.002 12l-3.75 6.495" />
                      </svg>                                        
                </div>
                <div class="flex flex-col">
                    <span class="text-lg text-slate-300 font-bold leading-5">Settings</span>
                    <span class="text-sm text-slate-500 hidden md:block">Edit App Settings</span>
                </div>
            </a>
            
           </div>
        </div>
        
      
    </div>
</div>'''
    },{
    "html":'''<script src="//unpkg.com/alpinejs" defer></script>

<main>
    <section class="bg-white dark:bg-gray-900">
    <nav x-data="{ isOpen: false }" class="container mx-auto p-6 lg:flex lg:items-center lg:justify-between">
        <div class="flex items-center justify-between">
        <div>
            <a class="text-2xl font-bold text-gray-800 hover:text-gray-700 dark:text-white dark:hover:text-gray-300 lg:text-3xl" href="#">Brand</a>
        </div>

        <!-- Mobile menu button -->
        <div class="flex lg:hidden">
            <button x-cloak @click="isOpen = !isOpen" type="button" class="text-gray-500 hover:text-gray-600 focus:text-gray-600 focus:outline-none dark:text-gray-200 dark:hover:text-gray-400 dark:focus:text-gray-400" aria-label="toggle menu">
            <svg x-show="!isOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 8h16M4 16h16" />
            </svg>

            <svg x-show="isOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
            </button>
        </div>
        </div>

        <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
        <div x-cloak :class="[isOpen ? 'translate-x-0 opacity-100 ' : 'opacity-0 -translate-x-full']" class="absolute inset-x-0 z-20 w-full bg-white px-6 py-4 shadow-md transition-all duration-300 ease-in-out dark:bg-gray-900 lg:relative lg:top-0 lg:mt-0 lg:flex lg:w-auto lg:translate-x-0 lg:items-center lg:bg-transparent lg:p-0 lg:opacity-100 lg:shadow-none lg:dark:bg-transparent">
        <div class="lg:-px-8 flex flex-col space-y-4 lg:mt-0 lg:flex-row lg:space-y-0">
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Home</a>
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Components</a>
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Pricing</a>
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Contact</a>
        </div>

        <a class="mt-4 block rounded-lg bg-blue-600 px-6 py-2.5 text-center font-medium capitalize leading-5 text-white hover:bg-blue-500 lg:mt-0 lg:w-auto" href="#"> Get started </a>
        </div>
    </nav>

    <div class="container mx-auto px-6 py-16 text-center">
        <div class="mx-auto max-w-lg">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white lg:text-4xl">Building Your Next App with our Awesome components</h1>
        <p class="mt-6 text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero similique obcaecati illum mollitia.</p>
        <button class="mt-6 rounded-lg bg-blue-600 px-6 py-2.5 text-center text-sm font-medium capitalize leading-5 text-white hover:bg-blue-500 focus:outline-none lg:mx-0 lg:w-auto">Start 14-Day free trial</button>
        <p class="mt-3 text-sm text-gray-400">No credit card required</p>
        </div>

        <div class="mt-10 flex justify-center">
        <img class="h-96 w-full rounded-xl object-cover lg:w-4/5" src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80" />
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">Portfolio</h1>

        <p class="mt-4 text-center text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nostrum quam voluptatibus</p>

        <div class="mt-8 grid grid-cols-1 gap-8 md:grid-cols-2 xl:mt-12 xl:grid-cols-3 xl:gap-12">
        <div>
            <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1621111848501-8d3634f82336?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1565&q=80" alt="" />
            <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Best website collections</h2>
            <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Website</p>
        </div>

        <div>
            <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1621609764180-2ca554a9d6f2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />
            <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Block of Ui kit collections</h2>
            <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Ui kit</p>
        </div>

        <div>
            <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />
            <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Ton’s of mobile mockup</h2>
            <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Mockups</p>
        </div>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="h-[32rem] bg-gray-100 dark:bg-gray-800">
        <div class="container mx-auto px-6 py-10">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">The Executive Team</h1>

        <div class="mx-auto mt-6 flex justify-center">
            <span class="inline-block h-1 w-40 rounded-full bg-blue-500"></span>
            <span class="mx-1 inline-block h-1 w-3 rounded-full bg-blue-500"></span>
            <span class="inline-block h-1 w-1 rounded-full bg-blue-500"></span>
        </div>

        <p class="mx-auto mt-6 max-w-2xl text-center text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo incidunt ex placeat modi magni quia error alias, adipisci rem similique, at omnis eligendi optio eos harum.</p>
        </div>
    </div>

    <div class="container mx-auto -mt-72 px-6 py-10 sm:-mt-80 md:-mt-96">
        <div class="mt-8 grid grid-cols-1 gap-8 md:grid-cols-2 xl:mt-16 xl:grid-cols-3">
        <div class="flex flex-col items-center rounded-xl border p-4 dark:border-gray-700 sm:p-6">
            <img class="aspect-square w-full rounded-xl object-cover" src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 dark:text-white">arthur melo</h1>

            <p class="mt-2 capitalize text-gray-500 dark:text-gray-300">design director</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="flex flex-col items-center rounded-xl border p-4 dark:border-gray-700 sm:p-6">
            <img class="aspect-square w-full rounded-xl object-cover" src="https://images.unsplash.com/photo-1531590878845-12627191e687?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 dark:text-white">Pamela Anderson</h1>

            <p class="mt-2 capitalize text-gray-500 dark:text-gray-300">Lead Developer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="flex flex-col items-center rounded-xl border p-4 dark:border-gray-700 sm:p-6">
            <img class="aspect-square w-full rounded-xl object-cover" src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 dark:text-white">John Doe</h1>

            <p class="mt-2 capitalize text-gray-500 dark:text-gray-300">Full stack developer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">What clients saying</h1>

        <div class="mx-auto mt-6 flex justify-center">
        <span class="inline-block h-1 w-40 rounded-full bg-blue-500"></span>
        <span class="mx-1 inline-block h-1 w-3 rounded-full bg-blue-500"></span>
        <span class="inline-block h-1 w-1 rounded-full bg-blue-500"></span>
        </div>

        <div class="mx-auto mt-16 flex max-w-6xl items-start">
        <button class="hidden rounded-full border p-2 text-gray-800 transition-colors duration-300 hover:bg-gray-100 rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 lg:block">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
        </button>

        <div>
            <p class="flex items-center text-center text-gray-500 lg:mx-8">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam, quam. Odio voluptatem officiis eos illo! Pariatur, totam alias. Beatae accusamus earum quos obcaecati minima molestias. Possimus minima dolores itaque! Esse! Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea voluptates fugiat corrupti laudantium dolores reiciendis pariatur esse quod nihil quia cupiditate debitis quisquam nemo, accusamus animi explicabo? Architecto, unde laboriosam?</p>

            <div class="mt-8 flex flex-col items-center justify-center">
            <img class="h-14 w-14 rounded-full object-cover" src="https://images.unsplash.com/photo-1499470932971-a90681ce8530?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <div class="mt-4 text-center">
                <h1 class="font-semibold text-gray-800 dark:text-white">Mia Brown</h1>
                <span class="text-sm text-gray-500 dark:text-gray-400">Marketer</span>
            </div>
            </div>
        </div>

        <button class="hidden rounded-full border p-2 text-gray-800 transition-colors duration-300 hover:bg-gray-100 rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 lg:block">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
            </svg>
        </button>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-10">
        <div class="text-center">
        <h1 class="text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">From the blog</h1>

        <p class="mx-auto mt-4 max-w-lg text-gray-500">Salami mustard spice tea fridge authentic Chinese food dish salt tasty liquor. Sweet savory foodtruck pie.</p>
        </div>

        <div class="mt-8 grid grid-cols-1 gap-8 md:mt-16 md:grid-cols-2 xl:grid-cols-3">
        <div>
            <div class="relative">
            <img class="h-64 w-full rounded-lg object-cover object-center lg:h-80" src="https://images.unsplash.com/photo-1624996379697-f01d168b1a52?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <div class="absolute bottom-0 flex bg-white p-3 dark:bg-gray-900">
                <img class="h-10 w-10 rounded-full object-cover object-center" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

                <div class="mx-4">
                <h1 class="text-sm text-gray-700 dark:text-gray-200">Tom Hank</h1>
                <p class="text-sm text-gray-500 dark:text-gray-400">Creative Director</p>
                </div>
            </div>
            </div>

            <h1 class="mt-6 text-xl font-semibold text-gray-800 dark:text-white">What do you want to know about UI</h1>

            <hr class="my-6 w-32 text-blue-500" />

            <p class="text-sm text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis fugit dolorum amet dolores praesentium, alias nam? Tempore</p>

            <a href="#" class="mt-4 inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
        </div>

        <div>
            <div class="relative">
            <img class="h-64 w-full rounded-lg object-cover object-center lg:h-80" src="https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <div class="absolute bottom-0 flex bg-white p-3 dark:bg-gray-900">
                <img class="h-10 w-10 rounded-full object-cover object-center" src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

                <div class="mx-4">
                <h1 class="text-sm text-gray-700 dark:text-gray-200">arthur melo</h1>
                <p class="text-sm text-gray-500 dark:text-gray-400">Creative Director</p>
                </div>
            </div>
            </div>

            <h1 class="mt-6 text-xl font-semibold text-gray-800 dark:text-white">All the features you want to know</h1>

            <hr class="my-6 w-32 text-blue-500" />

            <p class="text-sm text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis fugit dolorum amet dolores praesentium, alias nam? Tempore</p>

            <a href="#" class="mt-4 inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
        </div>

        <div>
            <div class="relative">
            <img class="h-64 w-full rounded-lg object-cover object-center lg:h-80" src="https://images.unsplash.com/photo-1597534458220-9fb4969f2df5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80" alt="" />

            <div class="absolute bottom-0 flex bg-white p-3 dark:bg-gray-900">
                <img class="h-10 w-10 rounded-full object-cover object-center" src="https://images.unsplash.com/photo-1531590878845-12627191e687?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />

                <div class="mx-4">
                <h1 class="text-sm text-gray-700 dark:text-gray-200">Amelia. Anderson</h1>
                <p class="text-sm text-gray-500 dark:text-gray-400">Lead Developer</p>
                </div>
            </div>
            </div>

            <h1 class="mt-6 text-xl font-semibold text-gray-800 dark:text-white">Which services you get from Meraki UI</h1>

            <hr class="my-6 w-32 text-blue-500" />

            <p class="text-sm text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis fugit dolorum amet dolores praesentium, alias nam? Tempore</p>

            <a href="#" class="mt-4 inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
        </div>
        </div>
    </div>
    </section>

    <div class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-8">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">Pricing Plan</h1>

        <p class="mx-auto mt-4 max-w-2xl text-center text-gray-500 dark:text-gray-300 xl:mt-6">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias quas magni libero consequuntur voluptatum velit amet id repudiandae ea, deleniti laborum in neque eveniet.</p>

        <div class="mt-6 grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3 xl:mt-12 xl:gap-12">
        <div class="w-full space-y-8 rounded-lg border border-gray-100 p-8 text-center dark:border-gray-700">
            <p class="font-medium uppercase text-gray-500 dark:text-gray-300">Free</p>

            <h2 class="text-5xl font-bold uppercase text-gray-800 dark:text-gray-100">$0</h2>

            <p class="font-medium text-gray-500 dark:text-gray-300">Life time</p>

            <button class="mt-10 w-full transform rounded-md bg-blue-600 px-4 py-2 capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">Start Now</button>
        </div>

        <div class="w-full space-y-8 rounded-lg bg-blue-600 p-8 text-center">
            <p class="font-medium uppercase text-gray-200">Premium</p>

            <h2 class="text-5xl font-bold uppercase text-white dark:text-gray-100">$40</h2>

            <p class="font-medium text-gray-200">Per month</p>

            <button class="mt-10 w-full transform rounded-md bg-white px-4 py-2 capitalize tracking-wide text-blue-500 transition-colors duration-300 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none focus:ring focus:ring-gray-200 focus:ring-opacity-80">Start Now</button>
        </div>

        <div class="w-full space-y-8 rounded-lg border border-gray-100 p-8 text-center dark:border-gray-700">
            <p class="font-medium uppercase text-gray-500 dark:text-gray-300">Enterprise</p>

            <h2 class="text-5xl font-bold uppercase text-gray-800 dark:text-gray-100">$100</h2>

            <p class="font-medium text-gray-500 dark:text-gray-300">Life time</p>

            <button class="mt-10 w-full transform rounded-md bg-blue-600 px-4 py-2 capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">Start Now</button>
        </div>
        </div>
    </div>
    </div>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto max-w-4xl px-6 py-10">
        <h1 class="text-center text-4xl font-semibold text-gray-800 dark:text-white">Frequently asked questions</h1>

        <div class="mt-12 space-y-8">
        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">How i can play for my appoinment ?</h1>

            <span class="rounded-full bg-gray-200 text-gray-400">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12H6" />
                </svg>
            </span>
            </button>

            <hr class="border-gray-200 dark:border-gray-700" />

            <p class="p-8 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas eaque nobis, fugit odit omnis fugiat deleniti animi ab maxime cum laboriosam recusandae facere dolorum veniam quia pariatur obcaecati illo ducimus?</p>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">Is the cost of the appoinment covered by private health insurance?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">Do i need a referral?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">What are your opening house?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">What can i expect at my first consultation?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>
        </div>
    </div>
    </section>

    <section class="min-h-screen bg-gradient-to-r from-blue-600 via-blue-800 to-blue-900 dark:from-gray-700 dark:via-gray-800 dark:to-gray-900">
    <div class="container mx-auto flex min-h-screen flex-col px-6 py-12">
        <div class="flex-1 lg:-mx-6 lg:flex lg:items-center">
        <div class="text-white lg:mx-6 lg:w-1/2">
            <h1 class="text-3xl font-semibold capitalize lg:text-5xl">Get a quote</h1>

            <p class="mt-6 max-w-xl">Ask us everything and we would love to hear from you</p>

            <div class="mt-6 space-y-8 md:mt-8">
            <p class="-mx-2 flex items-start">
                <svg xmlns="http://www.w3.org/2000/svg" class="mx-2 h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>

                <span class="mx-2 w-72 truncate text-white"> Cecilia Chapman 711-2880 Nulla St. Mankato Mississippi 96522 </span>
            </p>

            <p class="-mx-2 flex items-start">
                <svg xmlns="http://www.w3.org/2000/svg" class="mx-2 h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>

                <span class="mx-2 w-72 truncate text-white">(257) 563-7401</span>
            </p>

            <p class="-mx-2 flex items-start">
                <svg xmlns="http://www.w3.org/2000/svg" class="mx-2 h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>

                <span class="mx-2 w-72 truncate text-white">acb@example.com</span>
            </p>
            </div>

            <div class="mt-6 md:mt-8">
            <h3 class="text-gray-300">Follow us</h3>

            <div class="-mx-1.5 mt-4 flex">
                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-10 w-10 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M18.6668 6.67334C18.0002 7.00001 17.3468 7.13268 16.6668 7.33334C15.9195 6.49001 14.8115 6.44334 13.7468 6.84201C12.6822 7.24068 11.9848 8.21534 12.0002 9.33334V10C9.83683 10.0553 7.91016 9.07001 6.66683 7.33334C6.66683 7.33334 3.87883 12.2887 9.3335 14.6667C8.0855 15.498 6.84083 16.0587 5.3335 16C7.53883 17.202 9.94216 17.6153 12.0228 17.0113C14.4095 16.318 16.3708 14.5293 17.1235 11.85C17.348 11.0351 17.4595 10.1932 17.4548 9.34801C17.4535 9.18201 18.4615 7.50001 18.6668 6.67268V6.67334Z" />
                </svg>
                </a>

                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M15.2 8.80005C16.4731 8.80005 17.694 9.30576 18.5941 10.2059C19.4943 11.1061 20 12.327 20 13.6V19.2H16.8V13.6C16.8 13.1757 16.6315 12.7687 16.3314 12.4687C16.0313 12.1686 15.6244 12 15.2 12C14.7757 12 14.3687 12.1686 14.0687 12.4687C13.7686 12.7687 13.6 13.1757 13.6 13.6V19.2H10.4V13.6C10.4 12.327 10.9057 11.1061 11.8059 10.2059C12.7061 9.30576 13.927 8.80005 15.2 8.80005Z" fill="currentColor" />
                    <path d="M7.2 9.6001H4V19.2001H7.2V9.6001Z" fill="currentColor" />
                    <path d="M5.6 7.2C6.48366 7.2 7.2 6.48366 7.2 5.6C7.2 4.71634 6.48366 4 5.6 4C4.71634 4 4 4.71634 4 5.6C4 6.48366 4.71634 7.2 5.6 7.2Z" fill="currentColor" />
                </svg>
                </a>

                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 10.2222V13.7778H9.66667V20H13.2222V13.7778H15.8889L16.7778 10.2222H13.2222V8.44444C13.2222 8.2087 13.3159 7.9826 13.4826 7.81591C13.6493 7.64921 13.8754 7.55556 14.1111 7.55556H16.7778V4H14.1111C12.9324 4 11.8019 4.46825 10.9684 5.30175C10.1349 6.13524 9.66667 7.2657 9.66667 8.44444V10.2222H7Z" fill="currentColor" />
                </svg>
                </a>

                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M11.9294 7.72275C9.65868 7.72275 7.82715 9.55428 7.82715 11.825C7.82715 14.0956 9.65868 15.9271 11.9294 15.9271C14.2 15.9271 16.0316 14.0956 16.0316 11.825C16.0316 9.55428 14.2 7.72275 11.9294 7.72275ZM11.9294 14.4919C10.462 14.4919 9.26239 13.2959 9.26239 11.825C9.26239 10.354 10.4584 9.15799 11.9294 9.15799C13.4003 9.15799 14.5963 10.354 14.5963 11.825C14.5963 13.2959 13.3967 14.4919 11.9294 14.4919ZM17.1562 7.55495C17.1562 8.08692 16.7277 8.51178 16.1994 8.51178C15.6674 8.51178 15.2425 8.08335 15.2425 7.55495C15.2425 7.02656 15.671 6.59813 16.1994 6.59813C16.7277 6.59813 17.1562 7.02656 17.1562 7.55495ZM19.8731 8.52606C19.8124 7.24434 19.5197 6.10901 18.5807 5.17361C17.6453 4.23821 16.51 3.94545 15.2282 3.88118C13.9073 3.80621 9.94787 3.80621 8.62689 3.88118C7.34874 3.94188 6.21341 4.23464 5.27444 5.17004C4.33547 6.10544 4.04628 7.24077 3.98201 8.52249C3.90704 9.84347 3.90704 13.8029 3.98201 15.1238C4.04271 16.4056 4.33547 17.5409 5.27444 18.4763C6.21341 19.4117 7.34517 19.7045 8.62689 19.7687C9.94787 19.8437 13.9073 19.8437 15.2282 19.7687C16.51 19.708 17.6453 19.4153 18.5807 18.4763C19.5161 17.5409 19.8089 16.4056 19.8731 15.1238C19.9481 13.8029 19.9481 9.84704 19.8731 8.52606ZM18.1665 16.5412C17.8881 17.241 17.349 17.7801 16.6456 18.0621C15.5924 18.4799 13.0932 18.3835 11.9294 18.3835C10.7655 18.3835 8.26272 18.4763 7.21307 18.0621C6.51331 17.7837 5.9742 17.2446 5.69215 16.5412C5.27444 15.488 5.37083 12.9888 5.37083 11.825C5.37083 10.6611 5.27801 8.15832 5.69215 7.10867C5.97063 6.40891 6.50974 5.8698 7.21307 5.58775C8.26629 5.17004 10.7655 5.26643 11.9294 5.26643C13.0932 5.26643 15.596 5.17361 16.6456 5.58775C17.3454 5.86623 17.8845 6.40534 18.1665 7.10867C18.5843 8.16189 18.4879 10.6611 18.4879 11.825C18.4879 12.9888 18.5843 15.4916 18.1665 16.5412Z" fill="currentColor" />
                </svg>
                </a>
            </div>
            </div>
        </div>

        <div class="mt-8 lg:mx-6 lg:w-1/2">
            <div class="mx-auto w-full overflow-hidden rounded-xl bg-white px-8 py-10 shadow-2xl dark:bg-gray-900 lg:max-w-xl">
            <h1 class="text-2xl font-medium text-gray-700 dark:text-gray-200">Contact form</h1>

            <form class="mt-6">
                <div class="flex-1">
                <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Full Name</label>
                <input type="text" placeholder="John Doe" class="mt-2 block w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300" />
                </div>

                <div class="mt-6 flex-1">
                <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Email address</label>
                <input type="email" placeholder="johndoe@example.com" class="mt-2 block w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300" />
                </div>

                <div class="mt-6 w-full">
                <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Message</label>
                <textarea class="mt-2 block h-32 w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 placeholder-gray-400 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300 md:h-48" placeholder="Message"></textarea>
                </div>

                <button class="mt-6 w-full transform rounded-md bg-blue-600 px-6 py-3 text-sm font-medium capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-400 focus:ring-opacity-50">get in touch</button>
            </form>
            </div>
        </div>
        </div>
    </div>
    </section>

    <footer class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-12">
        <div class="md:-mx-3 md:flex md:items-center md:justify-between">
        <h1 class="text-3xl font-semibold tracking-tight text-gray-800 dark:text-white md:mx-3 xl:text-4xl">Subscribe our newsletter to get update.</h1>

        <div class="mt-6 shrink-0 md:mx-3 md:mt-0 md:w-auto">
            <a href="#" class="inline-flex w-full items-center justify-center rounded-lg bg-gray-800 px-4 py-2 text-sm text-white duration-300 hover:bg-gray-700 focus:ring focus:ring-gray-300 focus:ring-opacity-80">
            <span class="mx-2">Sign Up Now</span>

            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mx-2 h-6 w-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3" />
            </svg>
            </a>
        </div>
        </div>

        <hr class="my-6 border-gray-200 dark:border-gray-700 md:my-10" />

        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Quick Link</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Home</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Who We Are</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Our Philosophy</a>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Industries</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Retail & E-Commerce</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Information Technology</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Finance & Insurance</a>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Services</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Translation</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Proofreading & Editing</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Content Creation</a>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Contact Us</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">+880 768 473 4978</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">info@merakiui.com</a>
            </div>
        </div>
        </div>

        <hr class="my-6 border-gray-200 dark:border-gray-700 md:my-10" />

        <div class="flex flex-col items-center justify-between sm:flex-row">
        <a href="#" class="text-2xl font-bold text-gray-800 transition-colors duration-300 hover:text-gray-700 dark:text-white dark:hover:text-gray-300">Brand</a>

        <p class="mt-4 text-sm text-gray-500 dark:text-gray-300 sm:mt-0">© Copyright 2021. All Rights Reserved.</p>
        </div>
    </div>
    </footer>
</main>'''
    },{
    "html":'''<script src="//unpkg.com/alpinejs" defer></script>

<main>
    <section class="bg-white dark:bg-gray-900">
    <nav x-data="{ isOpen: false }" class="container mx-auto p-6 lg:flex lg:items-center lg:justify-between">
        <div class="flex items-center justify-between">
        <div>
            <a class="text-2xl font-bold text-gray-800 hover:text-gray-700 dark:text-white dark:hover:text-gray-300 lg:text-3xl" href="#">Brand</a>
        </div>

        <!-- Mobile menu button -->
        <div class="flex lg:hidden">
            <button x-cloak @click="isOpen = !isOpen" type="button" class="text-gray-500 hover:text-gray-600 focus:text-gray-600 focus:outline-none dark:text-gray-200 dark:hover:text-gray-400 dark:focus:text-gray-400" aria-label="toggle menu">
            <svg x-show="!isOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 8h16M4 16h16" />
            </svg>

            <svg x-show="isOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
            </button>
        </div>
        </div>

        <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
        <div x-cloak :class="[isOpen ? 'translate-x-0 opacity-100 ' : 'opacity-0 -translate-x-full']" class="absolute inset-x-0 z-20 w-full bg-white px-6 py-4 shadow-md transition-all duration-300 ease-in-out dark:bg-gray-900 lg:relative lg:top-0 lg:mt-0 lg:flex lg:w-auto lg:translate-x-0 lg:items-center lg:bg-transparent lg:p-0 lg:opacity-100 lg:shadow-none lg:dark:bg-transparent">
        <div class="lg:-px-8 flex flex-col space-y-4 lg:mt-0 lg:flex-row lg:space-y-0">
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Home</a>
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Components</a>
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Pricing</a>
            <a class="transform text-gray-700 transition-colors duration-300 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-8" href="#">Contact</a>
        </div>

        <a class="mt-4 block rounded-lg bg-blue-600 px-6 py-2.5 text-center font-medium capitalize leading-5 text-white hover:bg-blue-500 lg:mt-0 lg:w-auto" href="#"> Get started </a>
        </div>
    </nav>

    <div class="container mx-auto px-6 py-16 text-center">
        <div class="mx-auto max-w-lg">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-white lg:text-4xl">Building Your Next App with our Awesome components</h1>
        <p class="mt-6 text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero similique obcaecati illum mollitia.</p>
        <button class="mt-6 rounded-lg bg-blue-600 px-6 py-2.5 text-center text-sm font-medium capitalize leading-5 text-white hover:bg-blue-500 focus:outline-none lg:mx-0 lg:w-auto">Start 14-Day free trial</button>
        <p class="mt-3 text-sm text-gray-400">No credit card required</p>
        </div>

        <div class="mt-10 flex justify-center">
        <img class="h-96 w-full rounded-xl object-cover lg:w-4/5" src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80" />
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">Portfolio</h1>

        <p class="mt-4 text-center text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nostrum quam voluptatibus</p>

        <div class="mt-8 grid grid-cols-1 gap-8 md:grid-cols-2 xl:mt-12 xl:grid-cols-3 xl:gap-12">
        <div>
            <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1621111848501-8d3634f82336?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1565&q=80" alt="" />
            <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Best website collections</h2>
            <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Website</p>
        </div>

        <div>
            <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1621609764180-2ca554a9d6f2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />
            <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Block of Ui kit collections</h2>
            <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Ui kit</p>
        </div>

        <div>
            <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />
            <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Ton’s of mobile mockup</h2>
            <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Mockups</p>
        </div>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="h-[32rem] bg-gray-100 dark:bg-gray-800">
        <div class="container mx-auto px-6 py-10">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">The Executive Team</h1>

        <div class="mx-auto mt-6 flex justify-center">
            <span class="inline-block h-1 w-40 rounded-full bg-blue-500"></span>
            <span class="mx-1 inline-block h-1 w-3 rounded-full bg-blue-500"></span>
            <span class="inline-block h-1 w-1 rounded-full bg-blue-500"></span>
        </div>

        <p class="mx-auto mt-6 max-w-2xl text-center text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo incidunt ex placeat modi magni quia error alias, adipisci rem similique, at omnis eligendi optio eos harum.</p>
        </div>
    </div>

    <div class="container mx-auto -mt-72 px-6 py-10 sm:-mt-80 md:-mt-96">
        <div class="mt-8 grid grid-cols-1 gap-8 md:grid-cols-2 xl:mt-16 xl:grid-cols-3">
        <div class="flex flex-col items-center rounded-xl border p-4 dark:border-gray-700 sm:p-6">
            <img class="aspect-square w-full rounded-xl object-cover" src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 dark:text-white">arthur melo</h1>

            <p class="mt-2 capitalize text-gray-500 dark:text-gray-300">design director</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="flex flex-col items-center rounded-xl border p-4 dark:border-gray-700 sm:p-6">
            <img class="aspect-square w-full rounded-xl object-cover" src="https://images.unsplash.com/photo-1531590878845-12627191e687?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 dark:text-white">Pamela Anderson</h1>

            <p class="mt-2 capitalize text-gray-500 dark:text-gray-300">Lead Developer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="flex flex-col items-center rounded-xl border p-4 dark:border-gray-700 sm:p-6">
            <img class="aspect-square w-full rounded-xl object-cover" src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 dark:text-white">John Doe</h1>

            <p class="mt-2 capitalize text-gray-500 dark:text-gray-300">Full stack developer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-10">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">What clients saying</h1>

        <div class="mx-auto mt-6 flex justify-center">
        <span class="inline-block h-1 w-40 rounded-full bg-blue-500"></span>
        <span class="mx-1 inline-block h-1 w-3 rounded-full bg-blue-500"></span>
        <span class="inline-block h-1 w-1 rounded-full bg-blue-500"></span>
        </div>

        <div class="mx-auto mt-16 flex max-w-6xl items-start">
        <button class="hidden rounded-full border p-2 text-gray-800 transition-colors duration-300 hover:bg-gray-100 rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 lg:block">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
        </button>

        <div>
            <p class="flex items-center text-center text-gray-500 lg:mx-8">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam, quam. Odio voluptatem officiis eos illo! Pariatur, totam alias. Beatae accusamus earum quos obcaecati minima molestias. Possimus minima dolores itaque! Esse! Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea voluptates fugiat corrupti laudantium dolores reiciendis pariatur esse quod nihil quia cupiditate debitis quisquam nemo, accusamus animi explicabo? Architecto, unde laboriosam?</p>

            <div class="mt-8 flex flex-col items-center justify-center">
            <img class="h-14 w-14 rounded-full object-cover" src="https://images.unsplash.com/photo-1499470932971-a90681ce8530?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <div class="mt-4 text-center">
                <h1 class="font-semibold text-gray-800 dark:text-white">Mia Brown</h1>
                <span class="text-sm text-gray-500 dark:text-gray-400">Marketer</span>
            </div>
            </div>
        </div>

        <button class="hidden rounded-full border p-2 text-gray-800 transition-colors duration-300 hover:bg-gray-100 rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 lg:block">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
            </svg>
        </button>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-10">
        <div class="text-center">
        <h1 class="text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">From the blog</h1>

        <p class="mx-auto mt-4 max-w-lg text-gray-500">Salami mustard spice tea fridge authentic Chinese food dish salt tasty liquor. Sweet savory foodtruck pie.</p>
        </div>

        <div class="mt-8 grid grid-cols-1 gap-8 md:mt-16 md:grid-cols-2 xl:grid-cols-3">
        <div>
            <div class="relative">
            <img class="h-64 w-full rounded-lg object-cover object-center lg:h-80" src="https://images.unsplash.com/photo-1624996379697-f01d168b1a52?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <div class="absolute bottom-0 flex bg-white p-3 dark:bg-gray-900">
                <img class="h-10 w-10 rounded-full object-cover object-center" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

                <div class="mx-4">
                <h1 class="text-sm text-gray-700 dark:text-gray-200">Tom Hank</h1>
                <p class="text-sm text-gray-500 dark:text-gray-400">Creative Director</p>
                </div>
            </div>
            </div>

            <h1 class="mt-6 text-xl font-semibold text-gray-800 dark:text-white">What do you want to know about UI</h1>

            <hr class="my-6 w-32 text-blue-500" />

            <p class="text-sm text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis fugit dolorum amet dolores praesentium, alias nam? Tempore</p>

            <a href="#" class="mt-4 inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
        </div>

        <div>
            <div class="relative">
            <img class="h-64 w-full rounded-lg object-cover object-center lg:h-80" src="https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <div class="absolute bottom-0 flex bg-white p-3 dark:bg-gray-900">
                <img class="h-10 w-10 rounded-full object-cover object-center" src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

                <div class="mx-4">
                <h1 class="text-sm text-gray-700 dark:text-gray-200">arthur melo</h1>
                <p class="text-sm text-gray-500 dark:text-gray-400">Creative Director</p>
                </div>
            </div>
            </div>

            <h1 class="mt-6 text-xl font-semibold text-gray-800 dark:text-white">All the features you want to know</h1>

            <hr class="my-6 w-32 text-blue-500" />

            <p class="text-sm text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis fugit dolorum amet dolores praesentium, alias nam? Tempore</p>

            <a href="#" class="mt-4 inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
        </div>

        <div>
            <div class="relative">
            <img class="h-64 w-full rounded-lg object-cover object-center lg:h-80" src="https://images.unsplash.com/photo-1597534458220-9fb4969f2df5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80" alt="" />

            <div class="absolute bottom-0 flex bg-white p-3 dark:bg-gray-900">
                <img class="h-10 w-10 rounded-full object-cover object-center" src="https://images.unsplash.com/photo-1531590878845-12627191e687?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />

                <div class="mx-4">
                <h1 class="text-sm text-gray-700 dark:text-gray-200">Amelia. Anderson</h1>
                <p class="text-sm text-gray-500 dark:text-gray-400">Lead Developer</p>
                </div>
            </div>
            </div>

            <h1 class="mt-6 text-xl font-semibold text-gray-800 dark:text-white">Which services you get from Meraki UI</h1>

            <hr class="my-6 w-32 text-blue-500" />

            <p class="text-sm text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis fugit dolorum amet dolores praesentium, alias nam? Tempore</p>

            <a href="#" class="mt-4 inline-block text-blue-500 underline hover:text-blue-400">Read more</a>
        </div>
        </div>
    </div>
    </section>

    <div class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-8">
        <h1 class="text-center text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">Pricing Plan</h1>

        <p class="mx-auto mt-4 max-w-2xl text-center text-gray-500 dark:text-gray-300 xl:mt-6">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias quas magni libero consequuntur voluptatum velit amet id repudiandae ea, deleniti laborum in neque eveniet.</p>

        <div class="mt-6 grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3 xl:mt-12 xl:gap-12">
        <div class="w-full space-y-8 rounded-lg border border-gray-100 p-8 text-center dark:border-gray-700">
            <p class="font-medium uppercase text-gray-500 dark:text-gray-300">Free</p>

            <h2 class="text-5xl font-bold uppercase text-gray-800 dark:text-gray-100">$0</h2>

            <p class="font-medium text-gray-500 dark:text-gray-300">Life time</p>

            <button class="mt-10 w-full transform rounded-md bg-blue-600 px-4 py-2 capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">Start Now</button>
        </div>

        <div class="w-full space-y-8 rounded-lg bg-blue-600 p-8 text-center">
            <p class="font-medium uppercase text-gray-200">Premium</p>

            <h2 class="text-5xl font-bold uppercase text-white dark:text-gray-100">$40</h2>

            <p class="font-medium text-gray-200">Per month</p>

            <button class="mt-10 w-full transform rounded-md bg-white px-4 py-2 capitalize tracking-wide text-blue-500 transition-colors duration-300 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none focus:ring focus:ring-gray-200 focus:ring-opacity-80">Start Now</button>
        </div>

        <div class="w-full space-y-8 rounded-lg border border-gray-100 p-8 text-center dark:border-gray-700">
            <p class="font-medium uppercase text-gray-500 dark:text-gray-300">Enterprise</p>

            <h2 class="text-5xl font-bold uppercase text-gray-800 dark:text-gray-100">$100</h2>

            <p class="font-medium text-gray-500 dark:text-gray-300">Life time</p>

            <button class="mt-10 w-full transform rounded-md bg-blue-600 px-4 py-2 capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">Start Now</button>
        </div>
        </div>
    </div>
    </div>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto max-w-4xl px-6 py-10">
        <h1 class="text-center text-4xl font-semibold text-gray-800 dark:text-white">Frequently asked questions</h1>

        <div class="mt-12 space-y-8">
        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">How i can play for my appoinment ?</h1>

            <span class="rounded-full bg-gray-200 text-gray-400">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12H6" />
                </svg>
            </span>
            </button>

            <hr class="border-gray-200 dark:border-gray-700" />

            <p class="p-8 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas eaque nobis, fugit odit omnis fugiat deleniti animi ab maxime cum laboriosam recusandae facere dolorum veniam quia pariatur obcaecati illo ducimus?</p>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">Is the cost of the appoinment covered by private health insurance?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">Do i need a referral?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">What are your opening house?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>

        <div class="rounded-lg border-2 border-gray-100 dark:border-gray-700">
            <button class="flex w-full items-center justify-between p-8">
            <h1 class="font-semibold text-gray-700 dark:text-white">What can i expect at my first consultation?</h1>

            <span class="rounded-full bg-blue-500 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
            </span>
            </button>
        </div>
        </div>
    </div>
    </section>

    <section class="min-h-screen bg-gradient-to-r from-blue-600 via-blue-800 to-blue-900 dark:from-gray-700 dark:via-gray-800 dark:to-gray-900">
    <div class="container mx-auto flex min-h-screen flex-col px-6 py-12">
        <div class="flex-1 lg:-mx-6 lg:flex lg:items-center">
        <div class="text-white lg:mx-6 lg:w-1/2">
            <h1 class="text-3xl font-semibold capitalize lg:text-5xl">Get a quote</h1>

            <p class="mt-6 max-w-xl">Ask us everything and we would love to hear from you</p>

            <div class="mt-6 space-y-8 md:mt-8">
            <p class="-mx-2 flex items-start">
                <svg xmlns="http://www.w3.org/2000/svg" class="mx-2 h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>

                <span class="mx-2 w-72 truncate text-white"> Cecilia Chapman 711-2880 Nulla St. Mankato Mississippi 96522 </span>
            </p>

            <p class="-mx-2 flex items-start">
                <svg xmlns="http://www.w3.org/2000/svg" class="mx-2 h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>

                <span class="mx-2 w-72 truncate text-white">(257) 563-7401</span>
            </p>

            <p class="-mx-2 flex items-start">
                <svg xmlns="http://www.w3.org/2000/svg" class="mx-2 h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>

                <span class="mx-2 w-72 truncate text-white">acb@example.com</span>
            </p>
            </div>

            <div class="mt-6 md:mt-8">
            <h3 class="text-gray-300">Follow us</h3>

            <div class="-mx-1.5 mt-4 flex">
                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-10 w-10 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M18.6668 6.67334C18.0002 7.00001 17.3468 7.13268 16.6668 7.33334C15.9195 6.49001 14.8115 6.44334 13.7468 6.84201C12.6822 7.24068 11.9848 8.21534 12.0002 9.33334V10C9.83683 10.0553 7.91016 9.07001 6.66683 7.33334C6.66683 7.33334 3.87883 12.2887 9.3335 14.6667C8.0855 15.498 6.84083 16.0587 5.3335 16C7.53883 17.202 9.94216 17.6153 12.0228 17.0113C14.4095 16.318 16.3708 14.5293 17.1235 11.85C17.348 11.0351 17.4595 10.1932 17.4548 9.34801C17.4535 9.18201 18.4615 7.50001 18.6668 6.67268V6.67334Z" />
                </svg>
                </a>

                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M15.2 8.80005C16.4731 8.80005 17.694 9.30576 18.5941 10.2059C19.4943 11.1061 20 12.327 20 13.6V19.2H16.8V13.6C16.8 13.1757 16.6315 12.7687 16.3314 12.4687C16.0313 12.1686 15.6244 12 15.2 12C14.7757 12 14.3687 12.1686 14.0687 12.4687C13.7686 12.7687 13.6 13.1757 13.6 13.6V19.2H10.4V13.6C10.4 12.327 10.9057 11.1061 11.8059 10.2059C12.7061 9.30576 13.927 8.80005 15.2 8.80005Z" fill="currentColor" />
                    <path d="M7.2 9.6001H4V19.2001H7.2V9.6001Z" fill="currentColor" />
                    <path d="M5.6 7.2C6.48366 7.2 7.2 6.48366 7.2 5.6C7.2 4.71634 6.48366 4 5.6 4C4.71634 4 4 4.71634 4 5.6C4 6.48366 4.71634 7.2 5.6 7.2Z" fill="currentColor" />
                </svg>
                </a>

                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 10.2222V13.7778H9.66667V20H13.2222V13.7778H15.8889L16.7778 10.2222H13.2222V8.44444C13.2222 8.2087 13.3159 7.9826 13.4826 7.81591C13.6493 7.64921 13.8754 7.55556 14.1111 7.55556H16.7778V4H14.1111C12.9324 4 11.8019 4.46825 10.9684 5.30175C10.1349 6.13524 9.66667 7.2657 9.66667 8.44444V10.2222H7Z" fill="currentColor" />
                </svg>
                </a>

                <a class="mx-1.5 transform text-white transition-colors duration-300 hover:text-blue-500" href="#">
                <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M11.9294 7.72275C9.65868 7.72275 7.82715 9.55428 7.82715 11.825C7.82715 14.0956 9.65868 15.9271 11.9294 15.9271C14.2 15.9271 16.0316 14.0956 16.0316 11.825C16.0316 9.55428 14.2 7.72275 11.9294 7.72275ZM11.9294 14.4919C10.462 14.4919 9.26239 13.2959 9.26239 11.825C9.26239 10.354 10.4584 9.15799 11.9294 9.15799C13.4003 9.15799 14.5963 10.354 14.5963 11.825C14.5963 13.2959 13.3967 14.4919 11.9294 14.4919ZM17.1562 7.55495C17.1562 8.08692 16.7277 8.51178 16.1994 8.51178C15.6674 8.51178 15.2425 8.08335 15.2425 7.55495C15.2425 7.02656 15.671 6.59813 16.1994 6.59813C16.7277 6.59813 17.1562 7.02656 17.1562 7.55495ZM19.8731 8.52606C19.8124 7.24434 19.5197 6.10901 18.5807 5.17361C17.6453 4.23821 16.51 3.94545 15.2282 3.88118C13.9073 3.80621 9.94787 3.80621 8.62689 3.88118C7.34874 3.94188 6.21341 4.23464 5.27444 5.17004C4.33547 6.10544 4.04628 7.24077 3.98201 8.52249C3.90704 9.84347 3.90704 13.8029 3.98201 15.1238C4.04271 16.4056 4.33547 17.5409 5.27444 18.4763C6.21341 19.4117 7.34517 19.7045 8.62689 19.7687C9.94787 19.8437 13.9073 19.8437 15.2282 19.7687C16.51 19.708 17.6453 19.4153 18.5807 18.4763C19.5161 17.5409 19.8089 16.4056 19.8731 15.1238C19.9481 13.8029 19.9481 9.84704 19.8731 8.52606ZM18.1665 16.5412C17.8881 17.241 17.349 17.7801 16.6456 18.0621C15.5924 18.4799 13.0932 18.3835 11.9294 18.3835C10.7655 18.3835 8.26272 18.4763 7.21307 18.0621C6.51331 17.7837 5.9742 17.2446 5.69215 16.5412C5.27444 15.488 5.37083 12.9888 5.37083 11.825C5.37083 10.6611 5.27801 8.15832 5.69215 7.10867C5.97063 6.40891 6.50974 5.8698 7.21307 5.58775C8.26629 5.17004 10.7655 5.26643 11.9294 5.26643C13.0932 5.26643 15.596 5.17361 16.6456 5.58775C17.3454 5.86623 17.8845 6.40534 18.1665 7.10867C18.5843 8.16189 18.4879 10.6611 18.4879 11.825C18.4879 12.9888 18.5843 15.4916 18.1665 16.5412Z" fill="currentColor" />
                </svg>
                </a>
            </div>
            </div>
        </div>

        <div class="mt-8 lg:mx-6 lg:w-1/2">
            <div class="mx-auto w-full overflow-hidden rounded-xl bg-white px-8 py-10 shadow-2xl dark:bg-gray-900 lg:max-w-xl">
            <h1 class="text-2xl font-medium text-gray-700 dark:text-gray-200">Contact form</h1>

            <form class="mt-6">
                <div class="flex-1">
                <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Full Name</label>
                <input type="text" placeholder="John Doe" class="mt-2 block w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300" />
                </div>

                <div class="mt-6 flex-1">
                <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Email address</label>
                <input type="email" placeholder="johndoe@example.com" class="mt-2 block w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300" />
                </div>

                <div class="mt-6 w-full">
                <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Message</label>
                <textarea class="mt-2 block h-32 w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 placeholder-gray-400 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300 md:h-48" placeholder="Message"></textarea>
                </div>

                <button class="mt-6 w-full transform rounded-md bg-blue-600 px-6 py-3 text-sm font-medium capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-400 focus:ring-opacity-50">get in touch</button>
            </form>
            </div>
        </div>
        </div>
    </div>
    </section>

    <footer class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-12">
        <div class="md:-mx-3 md:flex md:items-center md:justify-between">
        <h1 class="text-3xl font-semibold tracking-tight text-gray-800 dark:text-white md:mx-3 xl:text-4xl">Subscribe our newsletter to get update.</h1>

        <div class="mt-6 shrink-0 md:mx-3 md:mt-0 md:w-auto">
            <a href="#" class="inline-flex w-full items-center justify-center rounded-lg bg-gray-800 px-4 py-2 text-sm text-white duration-300 hover:bg-gray-700 focus:ring focus:ring-gray-300 focus:ring-opacity-80">
            <span class="mx-2">Sign Up Now</span>

            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mx-2 h-6 w-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3" />
            </svg>
            </a>
        </div>
        </div>

        <hr class="my-6 border-gray-200 dark:border-gray-700 md:my-10" />

        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Quick Link</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Home</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Who We Are</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Our Philosophy</a>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Industries</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Retail & E-Commerce</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Information Technology</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Finance & Insurance</a>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Services</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Translation</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Proofreading & Editing</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Content Creation</a>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Contact Us</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">+880 768 473 4978</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">info@merakiui.com</a>
            </div>
        </div>
        </div>

        <hr class="my-6 border-gray-200 dark:border-gray-700 md:my-10" />

        <div class="flex flex-col items-center justify-between sm:flex-row">
        <a href="#" class="text-2xl font-bold text-gray-800 transition-colors duration-300 hover:text-gray-700 dark:text-white dark:hover:text-gray-300">Brand</a>

        <p class="mt-4 text-sm text-gray-500 dark:text-gray-300 sm:mt-0">© Copyright 2021. All Rights Reserved.</p>
        </div>
    </div>
    </footer>
</main>'''
    },{
    "html":'''<nav class="flex dark:bg-slate-900 items-center relative justify-between bg-white px-5 py-6 w-full">
  <div>
    <svg width="41" height="39" viewBox="0 0 41 39" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path class="dark:fill-white" d="M8.63077 14.8549C8.82584 14.8549 9.01902 14.8165 9.19926 14.7418C9.37949 14.6672 9.54324 14.5578 9.68119 14.4198C9.81914 14.2819 9.92858 14.1182 10.0032 13.9379C10.0779 13.7577 10.1163 13.5645 10.1163 13.3695C10.1163 10.6116 11.2119 7.9667 13.162 6.0166C15.112 4.0665 17.757 2.97094 20.5148 2.97094C23.2727 2.97094 25.9176 4.0665 27.8677 6.0166C29.8178 7.9667 30.9134 10.6116 30.9134 13.3695C30.9172 13.7609 31.0754 14.1349 31.3537 14.4103C31.6317 14.6857 32.0074 14.8402 32.3989 14.8402C32.7903 14.8402 33.1659 14.6857 33.444 14.4103C33.7222 14.1349 33.8804 13.7609 33.8843 13.3695C33.8843 11.6138 33.5385 9.87525 32.8666 8.25319C32.1947 6.63113 31.21 5.15729 29.9685 3.91582C28.7269 2.67435 27.2531 1.68956 25.6311 1.01769C24.009 0.345811 22.2706 0 20.5148 0C18.7591 0 17.0207 0.345811 15.3985 1.01769C13.7765 1.68956 12.3027 2.67435 11.0612 3.91582C9.81972 5.15729 8.83494 6.63113 8.16305 8.25319C7.49118 9.87525 7.14537 11.6138 7.14537 13.3695C7.14537 13.7634 7.30187 14.1412 7.58043 14.4198C7.859 14.6984 8.23682 14.8549 8.63077 14.8549Z" fill="#1A1E2C" />
      <path class="dark:fill-white" d="M39.5293 17.8258H26.452C27.4202 16.5421 27.9432 14.9775 27.9415 13.3695C27.9415 11.3996 27.1589 9.51035 25.7661 8.11742C24.3731 6.72449 22.4838 5.94196 20.5139 5.94196C18.5442 5.94196 16.655 6.72449 15.262 8.11742C13.869 9.51035 13.0865 11.3996 13.0865 13.3695C13.0865 13.7635 13.243 14.1413 13.5216 14.4199C13.8002 14.6985 14.1781 14.855 14.5721 14.855C14.9661 14.855 15.344 14.6985 15.6225 14.4199C15.9011 14.1413 16.0576 13.7635 16.0576 13.3695C16.0576 12.488 16.3189 11.6264 16.8086 10.8935C17.2983 10.1606 17.9943 9.58942 18.8086 9.25209C19.6229 8.91477 20.519 8.8265 21.3834 8.99844C22.2479 9.17038 23.0421 9.59481 23.6652 10.218C24.2885 10.8413 24.713 11.6354 24.885 12.4998C25.0569 13.3643 24.9687 14.2604 24.6314 15.0746C24.294 15.889 23.7229 16.5851 22.99 17.0748C22.2571 17.5645 21.3955 17.8258 20.5141 17.8258H1.50039C1.30407 17.8239 1.1093 17.8608 0.927353 17.9347C0.745405 18.0084 0.579889 18.1175 0.440367 18.2556C0.300847 18.3938 0.190089 18.5581 0.114504 18.7393C0.0389171 18.9206 0 19.115 0 19.3113C0 19.5075 0.0389171 19.702 0.114504 19.8832C0.190089 20.0644 0.300847 20.2287 0.440367 20.367C0.579889 20.505 0.745405 20.6142 0.927353 20.6879C1.1093 20.7617 1.30407 20.7987 1.50039 20.7967H39.5293C39.9207 20.7929 40.2947 20.6346 40.5701 20.3564C40.8455 20.0784 41 19.7027 41 19.3113C41 18.9198 40.8455 18.5442 40.5701 18.2661C40.2947 17.9879 39.9207 17.8297 39.5293 17.8258Z" fill="#0346F2" />
      <path class="dark:fill-white" d="M32.3692 23.942C32.1742 23.942 31.981 23.9803 31.8007 24.055C31.6205 24.1296 31.4568 24.239 31.3188 24.377C31.1809 24.5149 31.0714 24.6786 30.9968 24.8589C30.9221 25.0391 30.8837 25.2323 30.8837 25.4274C30.8837 28.1852 29.7881 30.8301 27.838 32.7802C25.888 34.7303 23.243 35.8259 20.4852 35.8259C17.7273 35.8259 15.0824 34.7303 13.1323 32.7802C11.1822 30.8301 10.0866 28.1852 10.0866 25.4274C10.0828 25.036 9.92455 24.6619 9.64634 24.3865C9.36827 24.1111 8.99262 23.9566 8.6011 23.9566C8.20973 23.9566 7.83408 24.1111 7.55601 24.3865C7.2778 24.6619 7.11956 25.036 7.11571 25.4274C7.11571 27.1831 7.46155 28.9216 8.13336 30.5436C8.80532 32.1657 9.79004 33.6395 11.0315 34.881C12.2731 36.1225 13.7469 37.1072 15.3689 37.7791C16.991 38.451 18.7294 38.7968 20.4852 38.7968C22.2409 38.7968 23.9793 38.451 25.6015 37.7791C27.2235 37.1072 28.6973 36.1225 29.9388 34.881C31.1803 33.6395 32.1651 32.1657 32.8369 30.5436C33.5088 28.9216 33.8546 27.1831 33.8546 25.4274C33.8546 25.0334 33.6981 24.6556 33.4196 24.377C33.141 24.0985 32.7632 23.942 32.3692 23.942Z" fill="#1A1E2C" />
      <path class="dark:fill-white" d="M1.47071 20.971H14.548C13.5798 22.2547 13.0568 23.8193 13.0585 25.4274C13.0585 27.3973 13.8411 29.2865 15.2339 30.6794C16.6269 32.0723 18.5162 32.8549 20.4861 32.8549C22.4558 32.8549 24.345 32.0723 25.738 30.6794C27.131 29.2865 27.9135 27.3973 27.9135 25.4274C27.9135 25.0334 27.757 24.6555 27.4784 24.3769C27.1998 24.0983 26.8219 23.9418 26.4279 23.9418C26.0339 23.9418 25.656 24.0983 25.3775 24.3769C25.0989 24.6555 24.9424 25.0334 24.9424 25.4274C24.9424 26.3088 24.6811 27.1704 24.1914 27.9033C23.7017 28.6362 23.0057 29.2074 22.1914 29.5447C21.3771 29.882 20.481 29.9703 19.6166 29.7984C18.7521 29.6264 17.9579 29.202 17.3348 28.5788C16.7115 27.9555 16.287 27.1615 16.115 26.297C15.9431 25.4325 16.0313 24.5364 16.3686 23.7222C16.706 22.9078 17.2771 22.2117 18.01 21.722C18.7429 21.2323 19.6045 20.971 20.4859 20.971H39.4996C39.6959 20.9729 39.8907 20.936 40.0726 20.8622C40.2546 20.7885 40.4201 20.6793 40.5596 20.5412C40.6992 20.403 40.8099 20.2387 40.8855 20.0575C40.9611 19.8762 41 19.6818 41 19.4855C41 19.2893 40.9611 19.0948 40.8855 18.9136C40.8099 18.7324 40.6992 18.5681 40.5596 18.4299C40.4201 18.2918 40.2546 18.1826 40.0726 18.1089C39.8907 18.0351 39.6959 17.9981 39.4996 18.0001H1.47071C1.07935 18.0039 0.705326 18.1622 0.429928 18.4404C0.15453 18.7184 0 19.0941 0 19.4855C0 19.877 0.15453 20.2526 0.429928 20.5307C0.705326 20.8089 1.07935 20.9672 1.47071 20.971Z" fill="#0346F2" />
    </svg>
  </div>
  <ul id="drawer" role="menu" class="sm:gap-3 transition-left ease-[cubic-bezier(0.4, 0.0, 0.2, 1)] delay-150  sm:flex  flex flex-col cursor-pointer absolute min-h-screen -left-48 sm:static w-48 top-0 bg-white sm:shadow-none shadow-xl sm:bg-transparent sm:flex-row sm:w-auto sm:min-h-0 dark:bg-slate-900  ">
    <div class="sm:hidden p-6 mb-5 flex items-center justify-center">
      <svg width="41" height="39" viewBox="0 0 41 39" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M8.63077 14.8549C8.82584 14.8549 9.01902 14.8165 9.19926 14.7418C9.37949 14.6672 9.54324 14.5578 9.68119 14.4198C9.81914 14.2819 9.92858 14.1182 10.0032 13.9379C10.0779 13.7577 10.1163 13.5645 10.1163 13.3695C10.1163 10.6116 11.2119 7.9667 13.162 6.0166C15.112 4.0665 17.757 2.97094 20.5148 2.97094C23.2727 2.97094 25.9176 4.0665 27.8677 6.0166C29.8178 7.9667 30.9134 10.6116 30.9134 13.3695C30.9172 13.7609 31.0754 14.1349 31.3537 14.4103C31.6317 14.6857 32.0074 14.8402 32.3989 14.8402C32.7903 14.8402 33.1659 14.6857 33.444 14.4103C33.7222 14.1349 33.8804 13.7609 33.8843 13.3695C33.8843 11.6138 33.5385 9.87525 32.8666 8.25319C32.1947 6.63113 31.21 5.15729 29.9685 3.91582C28.7269 2.67435 27.2531 1.68956 25.6311 1.01769C24.009 0.345811 22.2706 0 20.5148 0C18.7591 0 17.0207 0.345811 15.3985 1.01769C13.7765 1.68956 12.3027 2.67435 11.0612 3.91582C9.81972 5.15729 8.83494 6.63113 8.16305 8.25319C7.49118 9.87525 7.14537 11.6138 7.14537 13.3695C7.14537 13.7634 7.30187 14.1412 7.58043 14.4198C7.859 14.6984 8.23682 14.8549 8.63077 14.8549Z" fill="#1A1E2C" />
        <path d="M39.5293 17.8258H26.452C27.4202 16.5421 27.9432 14.9775 27.9415 13.3695C27.9415 11.3996 27.1589 9.51035 25.7661 8.11742C24.3731 6.72449 22.4838 5.94196 20.5139 5.94196C18.5442 5.94196 16.655 6.72449 15.262 8.11742C13.869 9.51035 13.0865 11.3996 13.0865 13.3695C13.0865 13.7635 13.243 14.1413 13.5216 14.4199C13.8002 14.6985 14.1781 14.855 14.5721 14.855C14.9661 14.855 15.344 14.6985 15.6225 14.4199C15.9011 14.1413 16.0576 13.7635 16.0576 13.3695C16.0576 12.488 16.3189 11.6264 16.8086 10.8935C17.2983 10.1606 17.9943 9.58942 18.8086 9.25209C19.6229 8.91477 20.519 8.8265 21.3834 8.99844C22.2479 9.17038 23.0421 9.59481 23.6652 10.218C24.2885 10.8413 24.713 11.6354 24.885 12.4998C25.0569 13.3643 24.9687 14.2604 24.6314 15.0746C24.294 15.889 23.7229 16.5851 22.99 17.0748C22.2571 17.5645 21.3955 17.8258 20.5141 17.8258H1.50039C1.30407 17.8239 1.1093 17.8608 0.927353 17.9347C0.745405 18.0084 0.579889 18.1175 0.440367 18.2556C0.300847 18.3938 0.190089 18.5581 0.114504 18.7393C0.0389171 18.9206 0 19.115 0 19.3113C0 19.5075 0.0389171 19.702 0.114504 19.8832C0.190089 20.0644 0.300847 20.2287 0.440367 20.367C0.579889 20.505 0.745405 20.6142 0.927353 20.6879C1.1093 20.7617 1.30407 20.7987 1.50039 20.7967H39.5293C39.9207 20.7929 40.2947 20.6346 40.5701 20.3564C40.8455 20.0784 41 19.7027 41 19.3113C41 18.9198 40.8455 18.5442 40.5701 18.2661C40.2947 17.9879 39.9207 17.8297 39.5293 17.8258Z" fill="#0346F2" />
        <path d="M32.3692 23.942C32.1742 23.942 31.981 23.9803 31.8007 24.055C31.6205 24.1296 31.4568 24.239 31.3188 24.377C31.1809 24.5149 31.0714 24.6786 30.9968 24.8589C30.9221 25.0391 30.8837 25.2323 30.8837 25.4274C30.8837 28.1852 29.7881 30.8301 27.838 32.7802C25.888 34.7303 23.243 35.8259 20.4852 35.8259C17.7273 35.8259 15.0824 34.7303 13.1323 32.7802C11.1822 30.8301 10.0866 28.1852 10.0866 25.4274C10.0828 25.036 9.92455 24.6619 9.64634 24.3865C9.36827 24.1111 8.99262 23.9566 8.6011 23.9566C8.20973 23.9566 7.83408 24.1111 7.55601 24.3865C7.2778 24.6619 7.11956 25.036 7.11571 25.4274C7.11571 27.1831 7.46155 28.9216 8.13336 30.5436C8.80532 32.1657 9.79004 33.6395 11.0315 34.881C12.2731 36.1225 13.7469 37.1072 15.3689 37.7791C16.991 38.451 18.7294 38.7968 20.4852 38.7968C22.2409 38.7968 23.9793 38.451 25.6015 37.7791C27.2235 37.1072 28.6973 36.1225 29.9388 34.881C31.1803 33.6395 32.1651 32.1657 32.8369 30.5436C33.5088 28.9216 33.8546 27.1831 33.8546 25.4274C33.8546 25.0334 33.6981 24.6556 33.4196 24.377C33.141 24.0985 32.7632 23.942 32.3692 23.942Z" fill="#1A1E2C" />
        <path d="M1.47071 20.971H14.548C13.5798 22.2547 13.0568 23.8193 13.0585 25.4274C13.0585 27.3973 13.8411 29.2865 15.2339 30.6794C16.6269 32.0723 18.5162 32.8549 20.4861 32.8549C22.4558 32.8549 24.345 32.0723 25.738 30.6794C27.131 29.2865 27.9135 27.3973 27.9135 25.4274C27.9135 25.0334 27.757 24.6555 27.4784 24.3769C27.1998 24.0983 26.8219 23.9418 26.4279 23.9418C26.0339 23.9418 25.656 24.0983 25.3775 24.3769C25.0989 24.6555 24.9424 25.0334 24.9424 25.4274C24.9424 26.3088 24.6811 27.1704 24.1914 27.9033C23.7017 28.6362 23.0057 29.2074 22.1914 29.5447C21.3771 29.882 20.481 29.9703 19.6166 29.7984C18.7521 29.6264 17.9579 29.202 17.3348 28.5788C16.7115 27.9555 16.287 27.1615 16.115 26.297C15.9431 25.4325 16.0313 24.5364 16.3686 23.7222C16.706 22.9078 17.2771 22.2117 18.01 21.722C18.7429 21.2323 19.6045 20.971 20.4859 20.971H39.4996C39.6959 20.9729 39.8907 20.936 40.0726 20.8622C40.2546 20.7885 40.4201 20.6793 40.5596 20.5412C40.6992 20.403 40.8099 20.2387 40.8855 20.0575C40.9611 19.8762 41 19.6818 41 19.4855C41 19.2893 40.9611 19.0948 40.8855 18.9136C40.8099 18.7324 40.6992 18.5681 40.5596 18.4299C40.4201 18.2918 40.2546 18.1826 40.0726 18.1089C39.8907 18.0351 39.6959 17.9981 39.4996 18.0001H1.47071C1.07935 18.0039 0.705326 18.1622 0.429928 18.4404C0.15453 18.7184 0 19.0941 0 19.4855C0 19.877 0.15453 20.2526 0.429928 20.5307C0.705326 20.8089 1.07935 20.9672 1.47071 20.971Z" fill="#0346F2" />
      </svg>
    </div>
    <li class="font-medium text-sm p-3 hover:bg-slate-300 dark:hover:bg-slate-800 sm:p-0 sm:hover:bg-transparent text-primary">
      <a href="#" class="dark:text-white">Men</a>
    </li>
    <li class="font-medium text-sm p-3 cursor-pointer hover:bg-slate-300 dark:hover:bg-slate-800 sm:p-0 sm:hover:bg-transparent text-gray-600 hover:text-primary transition-colors">
      <a href="#" class="dark:text-white">Women</a>
    </li>
    <li class="font-medium text-sm p-3 cursor-pointer hover:bg-slate-300 dark:hover:bg-slate-800 sm:p-0 sm:hover:bg-transparent text-gray-600 hover:text-primary transition-colors">
      <a href="#" class="dark:text-white">Kids</a>
    </li>
  </ul>
  <div class="flex gap-3 items-center">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path  class="dark:fill-white" fill-rule="evenodd" clip-rule="evenodd" d="M16.9303 7C16.9621 6.92913 16.977 6.85189 16.9739 6.77432H17C16.8882 4.10591 14.6849 2 12.0049 2C9.325 2 7.12172 4.10591 7.00989 6.77432C6.9967 6.84898 6.9967 6.92535 7.00989 7H6.93171C5.65022 7 4.28034 7.84597 3.88264 10.1201L3.1049 16.3147C2.46858 20.8629 4.81062 22 7.86853 22H16.1585C19.2075 22 21.4789 20.3535 20.9133 16.3147L20.1444 10.1201C19.676 7.90964 18.3503 7 17.0865 7H16.9303ZM15.4932 7C15.4654 6.92794 15.4506 6.85153 15.4497 6.77432C15.4497 4.85682 13.8899 3.30238 11.9657 3.30238C10.0416 3.30238 8.48184 4.85682 8.48184 6.77432C8.49502 6.84898 8.49502 6.92535 8.48184 7H15.4932ZM9.097 12.1486C8.60889 12.1486 8.21321 11.7413 8.21321 11.2389C8.21321 10.7366 8.60889 10.3293 9.097 10.3293C9.5851 10.3293 9.98079 10.7366 9.98079 11.2389C9.98079 11.7413 9.5851 12.1486 9.097 12.1486ZM14.002 11.2389C14.002 11.7413 14.3977 12.1486 14.8858 12.1486C15.3739 12.1486 15.7696 11.7413 15.7696 11.2389C15.7696 10.7366 15.3739 10.3293 14.8858 10.3293C14.3977 10.3293 14.002 10.7366 14.002 11.2389Z" fill="#200E32" />
    </svg>

    <div class="h-10 w-10 hover:ring-4 user cursor-pointer relative ring-blue-700/30 rounded-full bg-cover bg-center bg-[url('https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80')]">
      
       <div class="drop-down  w-48 overflow-hidden bg-white rounded-md shadow absolute top-12 right-3">
        <ul>
          <li class="px-3 py-3 text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
            <span>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </span>
            <span> Setting </span>
          </li>
          <li class="px-3  py-3  text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
            <span>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
</svg>
            </span>
            <span> Wishlist </span>
          </li>
          <li class="px-3  py-3 text-sm font-medium flex items-center space-x-2 hover:bg-slate-400">
            <span>
         <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
</svg>
            </span>
            <span> Logout </span>
          </li>
      
        </ul>
      </div>
    </div>
    <div class="sm:hidden cursor-pointer" id="mobile-toggle">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path class="dark:stroke-white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
      </svg>
    </div>
  </div>
</nav>'''
    },{
    "html":'''<!-- component -->
<script src="//unpkg.com/alpinejs" defer></script>

<main>
    <header class="bg-white dark:bg-gray-900">
        <nav x-data="{ isOpen: false }" class="container mx-auto p-6 lg:flex lg:items-center lg:justify-between">
            <div class="flex items-center justify-between">
            <div>
                <a class="text-2xl font-bold text-gray-800 hover:text-gray-700 dark:text-white dark:hover:text-gray-300 lg:text-3xl" href="#">Brand</a>
            </div>

            <!-- Mobile menu button -->
            <div class="flex lg:hidden">
                <button x-cloak @click="isOpen = !isOpen" type="button" class="text-gray-500 hover:text-gray-600 focus:text-gray-600 focus:outline-none dark:text-gray-200 dark:hover:text-gray-400 dark:focus:text-gray-400" aria-label="toggle menu">
                <svg x-show="!isOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4 8h16M4 16h16" />
                </svg>

                <svg x-show="isOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
                </button>
            </div>
            </div>

            <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
            <div x-cloak :class="[isOpen ? 'translate-x-0 opacity-100 ' : 'opacity-0 -translate-x-full']" class="absolute inset-x-0 z-20 w-full bg-white px-6 py-4 shadow-md transition-all duration-300 ease-in-out dark:bg-gray-900 lg:relative lg:top-0 lg:mt-0 lg:flex lg:w-auto lg:translate-x-0 lg:items-center lg:bg-transparent lg:p-0 lg:opacity-100 lg:shadow-none lg:dark:bg-transparent">
            <div class="flex flex-col space-y-4 lg:mt-0 lg:flex-row lg:space-y-0">
                <a class="text-gray-700 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-6" href="#">Home</a>
                <a class="text-gray-700 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-6" href="#">Components</a>
                <a class="text-gray-700 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-6" href="#">Pricing</a>
                <a class="text-gray-700 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-6" href="#">Contact</a>
                <a class="text-gray-700 hover:text-blue-500 dark:text-gray-200 dark:hover:text-blue-400 lg:mx-6" href="#">FAQ</a>
            </div>

            <a class="mt-4 block h-10 transform rounded-md border px-5 py-2 text-center text-sm capitalize text-gray-700 transition-colors duration-300 hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700 lg:mt-0 lg:w-auto" href="#"> Contact Us </a>
            </div>
        </nav>

        <div class="container mx-auto px-6 py-16 pt-28 text-center">
            <div class="mx-auto max-w-lg">
            <h1 class="text-3xl font-bold text-gray-800 dark:text-white md:text-4xl">Create beautiful website layout with Meraki UI.</h1>

            <p class="mt-6 text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero similique obcaecati illum mollitia.</p>

            <div class="mx-auto mt-6 w-full max-w-sm rounded-md border bg-transparent focus-within:border-blue-400 focus-within:ring focus-within:ring-blue-300 focus-within:ring-opacity-40 dark:border-gray-700 dark:focus-within:border-blue-300">
                <form class="flex flex-col md:flex-row">
                <input type="email" placeholder="Enter your email address" class="m-1 h-10 flex-1 appearance-none border-none bg-transparent px-4 py-2 text-gray-700 placeholder-gray-400 focus:placeholder-transparent focus:outline-none focus:ring-0 dark:text-gray-200" />

                <button type="button" class="m-1 h-10 transform rounded-md bg-blue-500 px-4 py-2 text-white transition-colors duration-300 hover:bg-blue-400 focus:bg-blue-400 focus:outline-none">Join Us</button>
                </form>
            </div>
            </div>

            <div class="mx-auto mt-28 max-w-screen-xl">
            <div class="grid grid-cols-2 gap-8 md:grid-cols-6 lg:grid-cols-5">
                <div class="col-span-1 flex items-center justify-center md:col-span-2 lg:col-span-1">
                <svg class="h-12 fill-current text-gray-500 dark:text-gray-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 266 100">
                    <path fill="none" d="M0 0h266v100H0z"></path>
                    <path d="M140.021 49.597c-1.784 0-3.07.585-4.374 1.181v13.486c1.249.119 1.965.119 3.15.119 4.282 0 4.869-1.961 4.869-4.699v-6.441c0-2.022-.671-3.646-3.645-3.646zm-28.438-.736c-2.971 0-3.649 1.631-3.649 3.651v1.135h7.294v-1.135c0-2.02-.678-3.651-3.645-3.651zm-55.09 14.037c0 1.598.754 2.428 2.418 2.428 1.785 0 2.842-.582 4.145-1.18v-3.199h-3.903c-1.848 0-2.66.344-2.66 1.951zm111.191-13.301c-2.976 0-4.007 1.624-4.007 3.646v7.379c0 2.027 1.031 3.656 4.007 3.656 2.968 0 4.007-1.629 4.007-3.656v-7.379c-.001-2.022-1.04-3.646-4.007-3.646zM41.909 71.172h-8.748V49.998H28.79v-7.296h4.372V38.32c0-5.953 2.467-9.492 9.479-9.492h5.838v7.298H44.83c-2.73 0-2.91 1.02-2.91 2.923l-.011 3.652h6.61l-.773 7.296h-5.837v21.175zm29.897.055h-7.291l-.315-1.844c-3.329 1.844-6.3 2.143-8.26 2.143-5.347 0-8.193-3.572-8.193-8.512 0-5.828 3.321-7.908 9.262-7.908h6.047v-1.26c0-2.975-.341-3.848-4.916-3.848h-7.48l.731-7.296h8.176c10.038 0 12.239 3.171 12.239 11.203v17.322zm24.793-20.694c-4.537-.778-5.84-.949-8.023-.949-3.921 0-5.106.865-5.106 4.195v6.299c0 3.33 1.185 4.199 5.106 4.199 2.183 0 3.486-.174 8.023-.955v7.117c-3.974.891-6.563 1.125-8.751 1.125-9.392 0-13.125-4.939-13.125-12.074v-5.111c0-7.141 3.733-12.089 13.125-12.089 2.188 0 4.777.235 8.751 1.13v7.113zm27.376 8.957h-16.042v.588c0 3.33 1.186 4.199 5.106 4.199 3.524 0 5.675-.174 10.204-.955v7.117c-4.368.891-6.644 1.125-10.929 1.125-9.393 0-13.128-4.939-13.128-12.074v-5.844c0-6.243 2.771-11.356 12.396-11.356s12.393 5.054 12.393 11.356v5.844zm28.437.135c0 6.896-1.971 11.926-13.911 11.926-4.312 0-6.841-.379-11.6-1.111V31.02l8.745-1.459V43.35c1.89-.702 4.336-1.059 6.562-1.059 8.746 0 10.203 3.921 10.203 10.222v7.112zm28.033.15c0 5.949-2.456 11.719-12.732 11.719-10.281 0-12.783-5.77-12.783-11.719v-5.744c0-5.952 2.502-11.723 12.783-11.723 10.276 0 12.732 5.771 12.732 11.723v5.744zm28.014 0c0 5.949-2.459 11.719-12.733 11.719-10.281 0-12.783-5.77-12.783-11.719v-5.744c0-5.952 2.502-11.723 12.783-11.723 10.274 0 12.733 5.771 12.733 11.723v5.744zm28.749 11.397h-9.479l-8.017-13.383v13.383h-8.748V31.019l8.748-1.459v25.849l8.017-12.707h9.479l-8.752 13.867 8.752 14.603zm-41.512-21.575c-2.971 0-4.002 1.624-4.002 3.646v7.379c0 2.027 1.031 3.656 4.002 3.656 2.967 0 4.017-1.629 4.017-3.656v-7.379c0-2.022-1.05-3.646-4.017-3.646zm46.505 16.581c1.473 0 2.646 1.201 2.646 2.701 0 1.523-1.174 2.711-2.657 2.711-1.476 0-2.673-1.188-2.673-2.711 0-1.5 1.197-2.701 2.673-2.701h.011zm-.011.42c-1.187 0-2.158 1.021-2.158 2.281 0 1.283.972 2.291 2.169 2.291 1.198.012 2.155-1.008 2.155-2.279s-.957-2.293-2.155-2.293h-.011zm-.503 3.853h-.48v-3.014c.252-.035.492-.07.852-.07.456 0 .754.096.937.227.177.133.272.336.272.623 0 .398-.262.637-.585.734v.023c.263.049.442.287.503.73.07.469.143.648.19.746h-.503c-.071-.098-.144-.373-.204-.77-.07-.383-.264-.527-.648-.527h-.333v1.298zm0-1.668h.348c.394 0 .729-.145.729-.518 0-.264-.19-.527-.729-.527-.157 0-.266.012-.348.023v1.022z"></path>
                </svg>
                </div>

                <div class="col-span-1 flex items-center justify-center md:col-span-2 lg:col-span-1">
                <svg class="h-10 fill-current text-gray-500 dark:text-gray-300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 316 60">
                    <g transform="translate(9.259 4.552) scale(.4941)">
                    <path d="M52.1 102.1V82.5c20.8 0 36.8-20.6 28.9-42.4-3-8.1-9.4-14.6-17.5-17.5-21.8-7.9-42.4 8.1-42.4 28.9H1.5c0-33.1 32-58.9 66.7-48.1 15.2 4.7 27.2 16.8 31.9 31.9 10.8 34.8-14.9 66.8-48 66.8z"></path>
                    <path d="M32.6 63h19.5v19.5H32.6zm-15 34.5v-15h15v15h-15zM5 70h12.6v12.5H5z" fill-rule="evenodd"></path>
                    <path d="M181.5 30.2c-5.8-4-13-6.1-21.4-6.1h-18.3v58.1h18.3c8.4 0 15.6-2.1 21.4-6.4 3.2-2.2 5.7-5.4 7.4-9.3s2.6-8.5 2.6-13.7c0-5.1-.9-9.7-2.6-13.6-1.7-3.8-4.2-6.9-7.4-9zm-29 3.8h5.8c6.4 0 11.7 1.3 15.7 3.7 4.4 2.7 6.7 7.8 6.7 15.1 0 7.6-2.3 12.9-6.7 15.8-3.8 2.5-9.1 3.8-15.6 3.8h-5.8V34z"></path>
                    <use xlink:href="#A"></use>
                    <path d="M199 41.3h10.3v41H199zm47.8 3.4c-3.1-2.8-6.6-4.4-10.3-4.4-5.7 0-10.4 2-14.1 5.8s-5.5 8.8-5.5 14.7c0 5.8 1.8 10.7 5.5 14.7 3.7 3.8 8.4 5.8 14.1 5.8 4 0 7.4-1.1 10.2-3.3v1c0 3.4-.9 6-2.7 7.9-1.8 1.8-4.3 2.7-7.4 2.7-4.8 0-7.7-1.9-11.4-6.8l-7 6.7.2.3c1.5 2.1 3.8 4.2 6.9 6.2s6.9 3 11.5 3c6.1 0 11.1-1.9 14.7-5.6 3.7-3.7 5.5-8.7 5.5-14.9V41.3h-10.1v3.4zm-2.7 24.2c-1.8 2-4.1 3-7.1 3s-5.3-1-7-3c-1.8-2-2.7-4.7-2.7-8s.9-6.1 2.7-8.1 4.1-3.1 7-3.1c3 0 5.3 1 7.1 3.1 1.8 2 2.7 4.8 2.7 8.1s-1 6-2.7 8zm21.6-27.6H276v41h-10.3z"></path>
                    <use xlink:href="#A" x="66.7"></use>
                    <path d="M298.6 30.3h-10.1v11.1h-5.9v9.4h5.9v17c0 5.3 1.1 9.1 3.2 11.3s5.8 3.3 11.1 3.3c1.7 0 3.4-.1 5-.2h.5v-9.4l-3.5.2c-2.5 0-4.1-.4-4.9-1.3s-1.2-2.7-1.2-5.4V50.7h9.6v-9.4h-9.6v-11zm57.9-6.2h10.3v58.1h-10.3zm114.4 43.5c-1.8 2.1-3.7 3.9-5.2 4.8-1.4.9-3.2 1.4-5.3 1.4-3 0-5.5-1.1-7.5-3.4s-3-5.2-3-8.7 1-6.4 2.9-8.6c2-2.3 4.4-3.4 7.4-3.4 3.3 0 6.8 2.1 9.8 5.6l6.8-6.5c-4.4-5.8-10.1-8.5-16.9-8.5-5.7 0-10.6 2.1-14.6 6.1s-6 9.2-6 15.3 2 11.2 6 15.3 8.9 6.1 14.6 6.1c7.5 0 13.5-3.2 17.5-9.1l-6.5-6.4zM513.2 47c-1.5-2-3.5-3.7-5.9-4.9-2.5-1.2-5.3-1.8-8.5-1.8-5.8 0-10.5 2.1-14 6.3-3.4 4.2-5.2 9.3-5.2 15.4 0 6.2 1.9 11.3 5.7 15.3 3.7 3.9 8.8 5.9 14.9 5.9 6.9 0 12.7-2.8 16.9-8.4l.2-.3-6.7-6.5c-.6.8-1.5 1.6-2.3 2.4-1 1-2 1.7-3 2.2-1.5.8-3.3 1.1-5.2 1.1-2.9 0-5.2-.8-7-2.5-1.7-1.5-2.7-3.6-2.9-6.2h27.3l.1-3.8c0-2.7-.4-5.2-1.1-7.6-.7-2.3-1.8-4.5-3.3-6.6zm-22.5 9.7c.5-2 1.4-3.6 2.7-4.9 1.4-1.4 3.2-2.1 5.4-2.1 2.5 0 4.4.7 5.7 2.1 1.2 1.3 1.9 2.9 2.1 4.8h-15.9zm62.1-12.3c-3.1-2.7-7.4-4-12.8-4-3.4 0-6.6.8-9.5 2.2-2.7 1.4-5.3 3.6-7 6.6l.1.1 6.6 6.3c2.7-4.3 5.7-5.8 9.7-5.8 2.2 0 3.9.6 5.3 1.7s2 2.6 2 4.4v2c-2.6-.8-5.1-1.2-7.6-1.2-5.1 0-9.3 1.2-12.4 3.6s-4.7 5.9-4.7 10.2c0 3.8 1.3 7 4 9.3 2.7 2.2 6 3.4 9.9 3.4s7.6-1.6 10.9-4.3v3.4h10.1V55.9c.2-4.9-1.4-8.8-4.6-11.5zm-18.3 22.2c1.2-.8 2.8-1.2 4.9-1.2 2.5 0 5.1.5 7.8 1.5v4C545 73 542 74 538.3 74c-1.8 0-3.2-.4-4.1-1.2s-1.4-1.7-1.4-3 .6-2.4 1.7-3.2zm62.7-21.4c-2.9-3.2-6.9-4.8-12-4.8-4.1 0-7.4 1.2-9.9 3.5v-2.5h-10.1v41h10.3V59.7c0-3.1.7-5.6 2.2-7.3 1.5-1.8 3.4-2.6 6.1-2.6 2.3 0 4.1.8 5.4 2.3 1.3 1.6 2 3.7 2 6.4v23.7h10.3V58.5c0-5.6-1.4-10.1-4.3-13.3zm-253.6-.8c-3.1-2.7-7.4-4-12.8-4-3.4 0-6.6.8-9.5 2.2-2.7 1.4-5.3 3.6-7 6.6l.1.1 6.6 6.3c2.7-4.3 5.7-5.8 9.7-5.8 2.2 0 3.9.6 5.3 1.7s2 2.6 2 4.4v2c-2.6-.8-5.1-1.2-7.6-1.2-5.1 0-9.3 1.2-12.4 3.6s-4.7 5.9-4.7 10.2c0 3.8 1.3 7 4 9.3 2.7 2.2 6 3.4 9.9 3.4s7.6-1.6 10.9-4.3v3.4h10.1V55.9c.1-4.9-1.5-8.8-4.6-11.5zm-18.3 22.2c1.2-.8 2.8-1.2 4.9-1.2 2.5 0 5.1.5 7.8 1.5v4c-2.2 2.1-5.2 3.1-8.9 3.1-1.8 0-3.2-.4-4.1-1.2s-1.4-1.7-1.4-3 .5-2.4 1.7-3.2zm78.9 16.5c-16.5 0-30-13.4-30-30s13.4-30 30-30c16.5 0 30 13.4 30 30s-13.5 30-30 30zm0-49.3c-10.7 0-19.4 8.7-19.4 19.4s8.7 19.4 19.4 19.4 19.4-8.7 19.4-19.4-8.7-19.4-19.4-19.4z"></path>
                    </g>
                    <defs><path d="M204.3 23.4c-1.8 0-3.3.6-4.5 1.8s-1.9 2.7-1.9 4.4c0 1.8.6 3.3 1.9 4.5 1.2 1.2 2.7 1.9 4.5 1.9s3.3-.6 4.5-1.9c1.2-1.2 1.9-2.8 1.9-4.5 0-1.8-.6-3.3-1.9-4.4-1.2-1.2-2.8-1.8-4.5-1.8z"></path></defs>
                </svg>
                </div>

                <div class="col-span-1 flex items-center justify-center md:col-span-2 lg:col-span-1">
                <svg class="mt-2 h-8 fill-current text-gray-500 dark:text-gray-300" viewBox="0 0 398 120" xmlns="http://www.w3.org/2000/svg">
                    <g fill-rule="nonzero">
                    <path d="M247.292 94.106C224.124 111.016 190.526 120 161.608 120c-40.544 0-77.046-14.822-104.673-39.476-2.164-1.936-.235-4.583 2.369-3.082 29.806 17.15 66.66 27.475 104.731 27.475 25.677 0 53.906-5.271 79.884-16.163 3.923-1.646 7.21 2.545 3.373 5.352"></path>
                    <path d="M256.533 82.534c-2.965-3.771-19.551-1.787-27.003-.897-2.254.277-2.605-1.692-.57-3.122 13.233-9.265 34.922-6.587 37.447-3.487 2.54 3.13-.666 24.802-13.073 35.147-1.91 1.59-3.718.744-2.877-1.357 2.782-6.952 9.04-22.505 6.076-26.284zM230.05 13.058V4.063c.015-1.378 1.04-2.29 2.291-2.283l40.493-.007c1.295 0 2.335.94 2.335 2.268v7.726c-.015 1.29-1.113 2.983-3.053 5.668l-20.97 29.843c7.78-.182 16.022.985 23.093 4.939 1.596.897 2.027 2.217 2.152 3.516v9.607c0 1.32-1.457 2.86-2.987 2.057-12.458-6.507-29-7.214-42.776.08-1.405.745-2.884-.765-2.884-2.086v-9.133c0-1.459.03-3.961 1.508-6.186l24.302-34.738h-21.162c-1.295 0-2.327-.927-2.342-2.276zM82.354 69.294H70.042c-1.171-.08-2.108-.956-2.203-2.072l.014-63.006c0-1.262 1.062-2.268 2.38-2.268L81.71 1.94c1.2.059 2.159.963 2.232 2.116v8.221h.234C87.163 4.326 92.8.613 100.39.613c7.708 0 12.539 3.713 15.98 11.664C119.361 4.326 126.14.613 133.393.613c5.175 0 10.804 2.123 14.251 6.893 3.916 5.311 3.111 12.993 3.111 19.755l-.015 39.764c0 1.255-1.061 2.262-2.379 2.262h-12.304c-1.23-.08-2.203-1.05-2.203-2.262l-.007-33.41c0-2.648.234-9.28-.344-11.796-.923-4.246-3.675-5.435-7.24-5.435-2.986 0-6.09 1.985-7.356 5.165-1.266 3.188-1.15 8.484-1.15 12.066v33.403c0 1.255-1.06 2.262-2.378 2.262h-12.297c-1.237-.08-2.21-1.051-2.21-2.262l-.015-33.41c0-7.025 1.142-17.362-7.59-17.362-8.858 0-8.506 10.074-8.506 17.362l-.007 33.403c-.022 1.276-1.084 2.283-2.401 2.283zm227.788-55.82c-9.084 0-9.662 12.328-9.662 20.017s-.117 24.131 9.545 24.131c9.545 0 10.006-13.262 10.006-21.345 0-5.303-.234-11.664-1.845-16.705-1.383-4.377-4.143-6.098-8.044-6.098zM310.025.613c18.284 0 28.173 15.647 28.173 35.533 0 19.222-10.92 34.468-28.173 34.468-17.933 0-27.712-15.647-27.712-35.132C282.305 15.86 292.2.612 310.025.612zm51.882 68.681h-12.275c-1.23-.08-2.211-1.05-2.211-2.261l-.015-63.028c.103-1.16 1.12-2.057 2.365-2.057l11.426-.008c1.076.059 1.961.788 2.188 1.766v9.636h.234c3.448-8.622 8.279-12.73 16.785-12.73 5.519 0 10.92 1.992 14.375 7.427C398 13.072 398 21.556 398 27.662v39.64c-.14 1.117-1.142 1.985-2.364 1.985h-12.349c-1.141-.073-2.064-.912-2.188-1.984V33.097c0-6.894.805-16.968-7.708-16.968-2.993 0-5.753 1.984-7.13 5.033-1.72 3.845-1.953 7.69-1.953 11.935v33.928c-.03 1.262-1.091 2.27-2.401 2.27zm-151.715-.16c-.813.73-1.991.78-2.913.284-4.092-3.385-4.824-4.953-7.064-8.177-6.756 6.864-11.543 8.921-20.305 8.921-10.372 0-18.438-6.376-18.438-19.134 0-9.965 5.424-16.742 13.139-20.061 6.683-2.925 16.023-3.458 23.167-4.253v-1.598c0-2.925.234-6.375-1.5-8.9-1.501-2.26-4.378-3.195-6.918-3.195-4.692 0-8.871 2.4-9.904 7.375-.212 1.11-1.024 2.204-2.137 2.262l-11.938-1.291c-1.01-.234-2.13-1.029-1.838-2.568C166.288 4.362 179.37 0 191.087 0c5.995 0 13.827 1.59 18.556 6.113 5.995 5.58 5.416 13.021 5.416 21.126v19.127c0 5.756 2.401 8.28 4.648 11.373.79 1.116.967 2.444-.036 3.26-2.518 2.102-6.983 5.968-9.443 8.15l-.036-.015zm-12.414-29.931v-2.656c-8.908 0-18.322 1.897-18.322 12.35 0 5.319 2.767 8.908 7.488 8.908 3.455 0 6.566-2.123 8.528-5.58 2.423-4.254 2.306-8.237 2.306-13.022zM48.72 69.133c-.813.73-1.991.781-2.913.285-4.092-3.385-4.824-4.953-7.064-8.177-6.763 6.864-11.55 8.921-20.305 8.921C8.06 70.162 0 63.786 0 51.028c0-9.965 5.417-16.742 13.139-20.061 6.683-2.925 16.015-3.458 23.16-4.253v-1.598c0-2.925.233-6.375-1.501-8.9-1.5-2.26-4.377-3.195-6.91-3.195-4.7 0-8.879 2.4-9.904 7.375-.212 1.11-1.024 2.204-2.137 2.262L3.91 21.367c-1.01-.234-2.13-1.029-1.845-2.568C4.81 4.362 17.89.007 29.615.007c5.995 0 13.827 1.59 18.556 6.113 5.995 5.581 5.416 13.022 5.416 21.126v19.128c0 5.755 2.401 8.28 4.648 11.372.79 1.116.967 2.444-.036 3.261-2.518 2.101-6.99 5.967-9.45 8.148l-.03-.021zm-12.422-29.93v-2.656c-8.908 0-18.32 1.897-18.32 12.35 0 5.319 2.766 8.908 7.487 8.908 3.462 0 6.573-2.123 8.528-5.58 2.422-4.254 2.305-8.237 2.305-13.022z"></path>
                    </g>
                </svg>
                </div>

                <div class="col-span-1 flex items-center justify-center md:col-span-3 lg:col-span-1">
                <svg class="mt-1 h-5 fill-current text-gray-500 dark:text-gray-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 278.7 36.3">
                    <g><path class="st0" d="M238.1 14.4v21.9h7V21.7h25.6v14.6h7V14.4h-39.6m6.2-7.1h27c3.8-.7 6.5-4.1 7.3-7.3H237c.8 3.2 3.6 6.5 7.3 7.3m-27.5 29c3.5-1.5 5.4-4.1 6.2-7.1h-31.5V.1h-7.1v36.2h32.4M131.9 7.2h25c3.8-1.1 6.9-4 7.7-7.1H125v21.4h32.4V29H132c-4 1.1-7.4 3.8-9.1 7.3h41.5V14.4H132l-.1-7.2m-61.6.1h27c3.8-.7 6.6-4.1 7.3-7.3H62.9c.8 3.2 3.6 6.5 7.4 7.3m0 14.3h27c3.8-.7 6.6-4.1 7.3-7.3H62.9c.8 3.2 3.6 6.5 7.4 7.3m0 14.7h27c3.8-.7 6.6-4.1 7.3-7.3H62.9c.8 3.2 3.6 6.6 7.4 7.3M0 .1c.8 3.2 3.6 6.4 7.3 7.2h11.4l.6.2v28.7h7.1V7.5l.6-.2h11.4c3.8-1 6.5-4 7.3-7.2V0L0 .1"></path></g>
                </svg>
                </div>

                <div class="col-span-2 flex items-center justify-center md:col-span-3 lg:col-span-1">
                <svg class="h-8 fill-current text-gray-500 dark:text-gray-300" viewBox="0 0 2270 546" xmlns="http://www.w3.org/2000/svg">
                    <g fill-rule="evenodd">
                    <path d="M888.413 394.397l-31.127 144.717h-71.593L903.977 14.642h84.81l111.28 524.472h-72.371l-30.35-144.717H888.413zm100.373-58.364l-24.124-125.3c-7.003-35.797-14.007-82.463-19.441-119.828h-3.126c-5.434 38.13-13.242 86.365-20.22 119.827l-24.902 125.301h91.813zM1373.34.648v441.205c0 28.806 1.556 70.828 3.1 97.274h-63.02l-4.67-45.9h-2.334c-12.451 26.445-41.244 52.138-79.362 52.138-70.037 0-112.837-76.275-112.837-193.755 0-133.848 56.794-196.881 116.728-196.881 30.336 0 54.46 14.02 67.689 42.8h1.556V.648h73.15zm-73.163 304.258c0-6.991 0-15.551-.778-23.359-3.89-34.227-23.345-63.798-49.79-63.798-45.927 0-61.477 63.798-61.477 133.848 0 77.818 20.232 132.278 59.142 132.278 16.342 0 38.118-8.56 50.569-53.681 1.556-6.226 2.334-15.577 2.334-24.111V304.906zm247.399 240.446c-75.471 0-129.957-64.59-129.957-194.52 0-137.752 64.576-196.116 133.835-196.116 74.705 0 128.387 66.924 128.387 194.546 0 150.19-73.927 196.09-131.5 196.09h-.765zm2.321-57.573c45.122 0 55.251-80.153 55.251-137.726 0-56.82-10.116-137.739-56.794-137.739-48.26 0-57.586 80.919-57.586 137.74 0 63.02 10.895 137.725 58.364 137.725h.765zM1723.938.648h73.137V203.74h1.556c19.455-34.227 45.913-49.025 79.375-49.025 64.577 0 105.055 73.15 105.055 189.099 0 135.391-55.25 201.537-117.506 201.537-37.353 0-58.364-20.246-74.719-53.708h-3.086l-3.904 47.47h-63.02c1.556-25.668 3.112-68.468 3.112-97.274V.648zm73.137 404.618c0 8.586.778 17.146 3.113 23.358 11.66 45.926 34.24 55.251 49.012 55.251 43.579 0 59.92-57.572 59.92-135.391 0-72.371-17.106-130.735-60.698-130.735-24.124 0-43.578 28.793-49.025 56.03-1.557 7.781-2.335 17.91-2.335 25.68v105.807h.013zm293.92-40.453c.779 97.273 42.788 121.384 87.145 121.384 26.458 0 49.025-6.213 65.367-14.007l10.895 52.916c-22.568 11.673-56.808 17.912-90.27 17.912-94.925 0-144.73-71.594-144.73-188.321 0-123.732 56.795-199.994 135.392-199.994s115.172 75.484 115.172 170.435c0 18.664-.792 30.35-1.557 40.453l-177.413-.778zm109.712-52.126c.778-66.924-22.567-102.707-51.347-102.707-38.144 0-55.264 55.251-57.586 102.707h108.933z" fill-rule="nonzero"></path>
                    <path d="M373.462 16.043h218.501v523.07L373.462 16.044zm-153.926 0H.88v523.07l218.657-523.07zm76.976 192.77l139.218 330.3H344.5l-41.633-105.197H200.964l95.548-225.103z"></path>
                    </g>
                </svg>
                </div>
            </div>
            </div>
        </div>
    </header>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 pt-28">
        <h1 class="text-2xl font-semibold text-gray-800 dark:text-white lg:text-4xl">Portfolio</h1>

        <div class="mt-8 lg:-mx-12 lg:flex xl:mt-16">
        <div class="lg:mx-12">
            <h1 class="text-xl font-semibold text-gray-800 dark:text-white">Table of Content</h1>

            <div class="mt-4 space-y-4 lg:mt-8">
            <a href="#" class="block text-blue-500 hover:underline dark:text-blue-400">Web design</a>
            <a href="#" class="block text-gray-500 hover:underline dark:text-gray-300">App design</a>
            <a href="#" class="block text-gray-500 hover:underline dark:text-gray-300">Branding</a>
            <a href="#" class="block text-gray-500 hover:underline dark:text-gray-300">Animation</a>
            </div>
        </div>

        <div class="mt-8 flex-1 lg:mx-12 lg:mt-0">
            <div class="grid grid-cols-1 gap-8 md:grid-cols-2 xl:grid-cols-3">
            <div>
                <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1621111848501-8d3634f82336?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1565&q=80" alt="" />
                <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Best website collections</h2>
                <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Website</p>
            </div>

            <div>
                <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1621609764180-2ca554a9d6f2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />
                <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Block of Ui kit collections</h2>
                <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Ui kit</p>
            </div>

            <div>
                <img class="h-96 w-full rounded-lg object-cover" src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />
                <h2 class="mt-4 text-2xl font-semibold capitalize text-gray-800 dark:text-white">Ton’s of mobile mockup</h2>
                <p class="mt-2 text-lg uppercase tracking-wider text-blue-500 dark:text-blue-400">Mockups</p>
            </div>
            </div>
        </div>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 pt-28">
        <h1 class="text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">Our Executive Team</h1>

        <p class="my-6 max-w-2xl text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo incidunt ex placeat modi magni quia error alias, adipisci rem similique, at omnis eligendi optio eos harum.</p>

        <div class="mt-8 grid grid-cols-1 gap-8 md:grid-cols-2 xl:mt-16 xl:grid-cols-4">
        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">arthur melo</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">design director</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1531590878845-12627191e687?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">Amelia. Anderson</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">Lead Developer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1488508872907-592763824245?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">Olivia Wathan</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">Lead designer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">John Doe</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">Full stack developer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1499470932971-a90681ce8530?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">Mia</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">Graphic Designer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1608174386344-80898cec6beb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">Junior REIS</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">Products Managers</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">Joseph Gonzalez</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">Software engineer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>

        <div class="group flex transform cursor-pointer flex-col items-center rounded-xl p-8 transition-colors duration-300 hover:bg-blue-600">
            <img class="h-32 w-32 rounded-full object-cover ring-4 ring-gray-300" src="https://images.unsplash.com/photo-1521488741203-dcc320950ce5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80" alt="" />

            <h1 class="mt-4 text-2xl font-semibold capitalize text-gray-700 group-hover:text-white dark:text-white">Emma Doe</h1>

            <p class="mt-2 capitalize text-gray-500 group-hover:text-gray-300 dark:text-gray-300">Content Writer</p>

            <div class="-mx-2 mt-3 flex">
            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Reddit">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Facebook">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
                </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 hover:text-gray-500 group-hover:text-white dark:text-gray-300 dark:hover:text-gray-300" aria-label="Github">
                <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
                </svg>
            </a>
            </div>
        </div>
        </div>
    </div>
    </section>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 pt-28">
        <div class="mt-6 md:flex md:items-center md:justify-between">
        <div>
            <h1 class="text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-4xl">What our clients are saying</h1>

            <div class="mx-auto mt-6 flex">
            <span class="inline-block h-1 w-40 rounded-full bg-blue-500"></span>
            <span class="mx-1 inline-block h-1 w-3 rounded-full bg-blue-500"></span>
            <span class="inline-block h-1 w-1 rounded-full bg-blue-500"></span>
            </div>
        </div>

        <div class="mt-8 flex justify-between md:mt-0">
            <button title="left arrow" class="mx-3 rounded-full border p-2 text-gray-800 transition-colors duration-300 hover:bg-gray-100 rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
            </button>

            <button title="right arrow" class="rounded-full border p-2 text-gray-800 transition-colors duration-300 hover:bg-gray-100 rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
            </svg>
            </button>
        </div>
        </div>

        <section class="mt-8 grid grid-cols-1 gap-8 lg:grid-cols-2 xl:mt-12 xl:grid-cols-3">
        <div class="rounded-lg border p-8 dark:border-gray-700">
            <p class="leading-loose text-gray-500 dark:text-gray-400">“Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore quibusdam ducimus libero ad tempora doloribus expedita laborum saepe voluptas perferendis delectus assumenda rerum, culpa aperiam dolorum, obcaecati corrupti aspernatur a.”.</p>

            <div class="-mx-2 mt-8 flex items-center">
            <img class="mx-2 h-14 w-14 shrink-0 rounded-full object-cover ring-4 ring-gray-300 dark:ring-gray-700" src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80" alt="" />

            <div class="mx-2">
                <h1 class="font-semibold text-gray-800 dark:text-white">Robert</h1>
                <span class="text-sm text-gray-500 dark:text-gray-400">CTO, Robert Consultency</span>
            </div>
            </div>
        </div>

        <div class="rounded-lg border border-transparent bg-blue-500 p-8 dark:bg-blue-600">
            <p class="leading-loose text-white">“Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore quibusdam ducimus libero ad tempora doloribus expedita laborum saepe voluptas perferendis delectus assumenda rerum, culpa aperiam dolorum, obcaecati corrupti aspernatur a.”.</p>

            <div class="-mx-2 mt-8 flex items-center">
            <img class="mx-2 h-14 w-14 shrink-0 rounded-full object-cover ring-4 ring-blue-200" src="https://images.unsplash.com/photo-1531590878845-12627191e687?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80" alt="" />

            <div class="mx-2">
                <h1 class="font-semibold text-white">Jeny Doe</h1>
                <span class="text-sm text-blue-200">CEO, Jeny Consultency</span>
            </div>
            </div>
        </div>

        <div class="rounded-lg border p-8 dark:border-gray-700">
            <p class="leading-loose text-gray-500 dark:text-gray-400">“Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore quibusdam ducimus libero ad tempora doloribus expedita laborum saepe voluptas perferendis delectus assumenda rerum, culpa aperiam dolorum, obcaecati corrupti aspernatur a.”.</p>

            <div class="-mx-2 mt-8 flex items-center">
            <img class="mx-2 h-14 w-14 shrink-0 rounded-full object-cover ring-4 ring-gray-300 dark:ring-gray-700" src="https://images.unsplash.com/photo-1488508872907-592763824245?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" alt="" />

            <div class="mx-2">
                <h1 class="font-semibold text-gray-800 dark:text-white">Ema Watson</h1>
                <span class="text-sm text-gray-500 dark:text-gray-400">Marketing Manager at Stech</span>
            </div>
            </div>
        </div>
        </section>
    </div>
    </section>

    <div class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 pt-28">
        <div class="xl:-mx-8 xl:flex xl:items-center">
        <div class="flex flex-col items-center xl:mx-8 xl:items-start">
            <h1 class="text-3xl font-medium capitalize text-gray-800 dark:text-white lg:text-4xl">Our Pricing Plan</h1>

            <div class="mt-4">
            <span class="inline-block h-1 w-40 rounded-full bg-blue-500"></span>
            <span class="mx-1 inline-block h-1 w-3 rounded-full bg-blue-500"></span>
            <span class="inline-block h-1 w-1 rounded-full bg-blue-500"></span>
            </div>

            <p class="mt-4 font-medium text-gray-500 dark:text-gray-300">You can get All Access by selecting your plan!</p>

            <a href="#" class="-mx-1 mt-4 flex items-center text-sm capitalize text-gray-700 hover:text-blue-600 hover:underline dark:text-blue-400 dark:hover:text-blue-500">
            <span class="mx-1">read more</span>
            <svg class="mx-1 h-4 w-4 rtl:-scale-x-100" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            </a>
        </div>

        <div class="flex-1 xl:mx-8">
            <div class="mt-8 space-y-8 md:-mx-4 md:flex md:items-center md:justify-center md:space-y-0 xl:mt-0">
            <div class="mx-auto max-w-sm rounded-lg border dark:border-gray-700 md:mx-4">
                <div class="p-6">
                <h1 class="text-xl font-medium capitalize text-gray-700 dark:text-white lg:text-3xl">Essential</h1>

                <p class="mt-4 text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nostrum quam voluptatibus</p>

                <h2 class="mt-4 text-2xl font-medium text-gray-700 dark:text-gray-300 sm:text-4xl">$3.00 <span class="text-base font-medium">/Month</span></h2>

                <p class="mt-1 text-gray-500 dark:text-gray-300">Yearly payment</p>

                <button class="mt-6 w-full transform rounded-md bg-blue-600 px-4 py-2 capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">Start Now</button>
                </div>

                <hr class="border-gray-200 dark:border-gray-700" />

                <div class="p-6">
                <h1 class="text-lg font-medium capitalize text-gray-700 dark:text-white lg:text-xl">What’s included:</h1>

                <div class="mt-8 space-y-4">
                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">All limited links</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Own analytics platform</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Chat support</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Optimize hashtags</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M13.477 14.89A6 6 0 015.11 6.524l8.367 8.368zm1.414-1.414L6.524 5.11a6 6 0 018.367 8.367zM18 10a8 8 0 11-16 0 8 8 0 0116 0z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Mobile app</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M13.477 14.89A6 6 0 015.11 6.524l8.367 8.368zm1.414-1.414L6.524 5.11a6 6 0 018.367 8.367zM18 10a8 8 0 11-16 0 8 8 0 0116 0z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Unlimited users</span>
                    </div>
                </div>
                </div>
            </div>

            <div class="mx-auto max-w-sm rounded-lg border dark:border-gray-700 md:mx-4">
                <div class="p-6">
                <h1 class="text-xl font-medium capitalize text-gray-700 dark:text-white lg:text-3xl">Premium</h1>

                <p class="mt-4 text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nostrum quam voluptatibus</p>

                <h2 class="mt-4 text-2xl font-medium text-gray-700 dark:text-gray-300 sm:text-4xl">$50.00 <span class="text-base font-medium">/life time</span></h2>

                <p class="mt-1 text-gray-500 dark:text-gray-300">One time payment</p>

                <button class="mt-6 w-full transform rounded-md bg-blue-600 px-4 py-2 capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-500 focus:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">Start Now</button>
                </div>

                <hr class="border-gray-200 dark:border-gray-700" />

                <div class="p-6">
                <h1 class="text-lg font-medium capitalize text-gray-700 dark:text-white lg:text-xl">What’s included:</h1>

                <div class="mt-8 space-y-4">
                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">All limited links</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Own analytics platform</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Chat support</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Optimize hashtags</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Mobile app</span>
                    </div>

                    <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>

                    <span class="mx-4 text-gray-700 dark:text-gray-300">Unlimited users</span>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </div>
    </div>

    <section class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-28">
        <h1 class="text-2xl font-semibold text-gray-800 dark:text-white lg:text-4xl">Frequently asked questions.</h1>

        <div class="mt-8 grid grid-cols-1 gap-8 md:grid-cols-2 lg:mt-16 xl:grid-cols-3">
        <div>
            <div class="inline-block rounded-lg bg-blue-600 p-3 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            </div>

            <div>
            <h1 class="text-xl font-semibold text-gray-700 dark:text-white">What can i expect at my first consultation?</h1>

            <p class="mt-2 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident placeat, consequatur eveniet veritatis quos dignissimos beatae dolores exercitationem laboriosam officia magnam atque blanditiis illum doloremque magni ex corrupti tempora quis.</p>
            </div>
        </div>

        <div>
            <div class="inline-block rounded-lg bg-blue-600 p-3 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            </div>

            <div>
            <h1 class="text-xl font-semibold text-gray-700 dark:text-white">What are your opening house?</h1>

            <p class="mt-2 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident placeat, consequatur eveniet veritatis quos dignissimos beatae dolores exercitationem laboriosam officia magnam atque blanditiis illum doloremque magni ex corrupti tempora quis.</p>
            </div>
        </div>

        <div>
            <div class="inline-block rounded-lg bg-blue-600 p-3 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            </div>

            <div>
            <h1 class="text-xl font-semibold text-gray-700 dark:text-white">Do i need a referral?</h1>

            <p class="mt-2 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident placeat, consequatur eveniet veritatis quos dignissimos beatae dolores exercitationem laboriosam officia magnam atque blanditiis illum doloremque magni ex corrupti tempora quis.</p>
            </div>
        </div>

        <div>
            <div class="inline-block rounded-lg bg-blue-600 p-3 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            </div>

            <div>
            <h1 class="text-xl font-semibold text-gray-700 dark:text-white">Is the cost of the appoinment covered by private health insurance?</h1>

            <p class="mt-2 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident placeat, consequatur eveniet veritatis quos dignissimos beatae dolores exercitationem laboriosam officia magnam atque blanditiis illum doloremque magni ex corrupti tempora quis.</p>
            </div>
        </div>

        <div>
            <div class="inline-block rounded-lg bg-blue-600 p-3 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            </div>

            <div>
            <h1 class="text-xl font-semibold text-gray-700 dark:text-white">What is your cancellation policy?</h1>

            <p class="mt-2 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident placeat, consequatur eveniet veritatis quos dignissimos beatae dolores exercitationem laboriosam officia magnam atque blanditiis illum doloremque magni ex corrupti tempora quis.</p>
            </div>
        </div>

        <div>
            <div class="inline-block rounded-lg bg-blue-600 p-3 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            </div>

            <div>
            <h1 class="text-xl font-semibold text-gray-700 dark:text-white">What are the parking and public transport options?</h1>

            <p class="mt-2 text-sm text-gray-500 dark:text-gray-300">Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident placeat, consequatur eveniet veritatis quos dignissimos beatae dolores exercitationem laboriosam officia magnam atque blanditiis illum doloremque magni ex corrupti tempora quis.</p>
            </div>
        </div>
        </div>
    </div>
    </section>

    <section class="min-h-screen bg-white dark:bg-gray-900 lg:flex">
    <div class="flex w-full flex-col justify-center p-8 lg:w-1/2 lg:bg-gray-100 lg:px-12 lg:dark:bg-gray-800 xl:px-32">
        <h1 class="text-3xl font-semibold capitalize text-gray-800 dark:text-white lg:text-5xl">hire us.</h1>

        <p class="mt-4 text-gray-500 dark:text-gray-400">Ask us everything and we would love to hear from you</p>

        <div class="mt-6 md:mt-8">
        <h3 class="font-medium text-gray-600 dark:text-gray-300">Follow us</h3>

        <div class="-mx-1.5 mt-4 flex">
            <a class="mx-1.5 transform text-gray-400 transition-colors duration-300 hover:text-blue-500 dark:hover:text-blue-400" href="#">
            <svg class="h-10 w-10 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M18.6668 6.67334C18.0002 7.00001 17.3468 7.13268 16.6668 7.33334C15.9195 6.49001 14.8115 6.44334 13.7468 6.84201C12.6822 7.24068 11.9848 8.21534 12.0002 9.33334V10C9.83683 10.0553 7.91016 9.07001 6.66683 7.33334C6.66683 7.33334 3.87883 12.2887 9.3335 14.6667C8.0855 15.498 6.84083 16.0587 5.3335 16C7.53883 17.202 9.94216 17.6153 12.0228 17.0113C14.4095 16.318 16.3708 14.5293 17.1235 11.85C17.348 11.0351 17.4595 10.1932 17.4548 9.34801C17.4535 9.18201 18.4615 7.50001 18.6668 6.67268V6.67334Z" />
            </svg>
            </a>

            <a class="mx-1.5 transform text-gray-400 transition-colors duration-300 hover:text-blue-500 dark:hover:text-blue-400" href="#">
            <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15.2 8.80005C16.4731 8.80005 17.694 9.30576 18.5941 10.2059C19.4943 11.1061 20 12.327 20 13.6V19.2H16.8V13.6C16.8 13.1757 16.6315 12.7687 16.3314 12.4687C16.0313 12.1686 15.6244 12 15.2 12C14.7757 12 14.3687 12.1686 14.0687 12.4687C13.7686 12.7687 13.6 13.1757 13.6 13.6V19.2H10.4V13.6C10.4 12.327 10.9057 11.1061 11.8059 10.2059C12.7061 9.30576 13.927 8.80005 15.2 8.80005Z" fill="currentColor" />
                <path d="M7.2 9.6001H4V19.2001H7.2V9.6001Z" fill="currentColor" />
                <path d="M5.6 7.2C6.48366 7.2 7.2 6.48366 7.2 5.6C7.2 4.71634 6.48366 4 5.6 4C4.71634 4 4 4.71634 4 5.6C4 6.48366 4.71634 7.2 5.6 7.2Z" fill="currentColor" />
            </svg>
            </a>

            <a class="mx-1.5 transform text-gray-400 transition-colors duration-300 hover:text-blue-500 dark:hover:text-blue-400" href="#">
            <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7 10.2222V13.7778H9.66667V20H13.2222V13.7778H15.8889L16.7778 10.2222H13.2222V8.44444C13.2222 8.2087 13.3159 7.9826 13.4826 7.81591C13.6493 7.64921 13.8754 7.55556 14.1111 7.55556H16.7778V4H14.1111C12.9324 4 11.8019 4.46825 10.9684 5.30175C10.1349 6.13524 9.66667 7.2657 9.66667 8.44444V10.2222H7Z" fill="currentColor" />
            </svg>
            </a>

            <a class="mx-1.5 transform text-gray-400 transition-colors duration-300 hover:text-blue-500 dark:hover:text-blue-400" href="#">
            <svg class="h-8 w-8" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M11.9294 7.72275C9.65868 7.72275 7.82715 9.55428 7.82715 11.825C7.82715 14.0956 9.65868 15.9271 11.9294 15.9271C14.2 15.9271 16.0316 14.0956 16.0316 11.825C16.0316 9.55428 14.2 7.72275 11.9294 7.72275ZM11.9294 14.4919C10.462 14.4919 9.26239 13.2959 9.26239 11.825C9.26239 10.354 10.4584 9.15799 11.9294 9.15799C13.4003 9.15799 14.5963 10.354 14.5963 11.825C14.5963 13.2959 13.3967 14.4919 11.9294 14.4919ZM17.1562 7.55495C17.1562 8.08692 16.7277 8.51178 16.1994 8.51178C15.6674 8.51178 15.2425 8.08335 15.2425 7.55495C15.2425 7.02656 15.671 6.59813 16.1994 6.59813C16.7277 6.59813 17.1562 7.02656 17.1562 7.55495ZM19.8731 8.52606C19.8124 7.24434 19.5197 6.10901 18.5807 5.17361C17.6453 4.23821 16.51 3.94545 15.2282 3.88118C13.9073 3.80621 9.94787 3.80621 8.62689 3.88118C7.34874 3.94188 6.21341 4.23464 5.27444 5.17004C4.33547 6.10544 4.04628 7.24077 3.98201 8.52249C3.90704 9.84347 3.90704 13.8029 3.98201 15.1238C4.04271 16.4056 4.33547 17.5409 5.27444 18.4763C6.21341 19.4117 7.34517 19.7045 8.62689 19.7687C9.94787 19.8437 13.9073 19.8437 15.2282 19.7687C16.51 19.708 17.6453 19.4153 18.5807 18.4763C19.5161 17.5409 19.8089 16.4056 19.8731 15.1238C19.9481 13.8029 19.9481 9.84704 19.8731 8.52606ZM18.1665 16.5412C17.8881 17.241 17.349 17.7801 16.6456 18.0621C15.5924 18.4799 13.0932 18.3835 11.9294 18.3835C10.7655 18.3835 8.26272 18.4763 7.21307 18.0621C6.51331 17.7837 5.9742 17.2446 5.69215 16.5412C5.27444 15.488 5.37083 12.9888 5.37083 11.825C5.37083 10.6611 5.27801 8.15832 5.69215 7.10867C5.97063 6.40891 6.50974 5.8698 7.21307 5.58775C8.26629 5.17004 10.7655 5.26643 11.9294 5.26643C13.0932 5.26643 15.596 5.17361 16.6456 5.58775C17.3454 5.86623 17.8845 6.40534 18.1665 7.10867C18.5843 8.16189 18.4879 10.6611 18.4879 11.825C18.4879 12.9888 18.5843 15.4916 18.1665 16.5412Z" fill="currentColor" />
            </svg>
            </a>
        </div>
        </div>
    </div>

    <div class="flex w-full flex-col justify-center p-8 pt-0 lg:w-1/2 lg:px-12 xl:px-24">
        <form>
        <div class="-mx-2 md:flex md:items-center">
            <div class="flex-1 px-2">
            <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Full Name</label>
            <input type="text" placeholder="John Doe" class="mt-2 block w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 placeholder-gray-400 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-400 focus:ring-opacity-40 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-300 dark:placeholder-gray-600 dark:focus:border-blue-400" />
            </div>

            <div class="mt-4 flex-1 px-2 md:mt-0">
            <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Email address</label>
            <input type="email" placeholder="johndoe@example.com" class="mt-2 block w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 placeholder-gray-400 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-400 focus:ring-opacity-40 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-300 dark:placeholder-gray-600 dark:focus:border-blue-400" />
            </div>
        </div>

        <div class="mt-4 w-full">
            <label class="mb-2 block text-sm text-gray-600 dark:text-gray-200">Message</label>
            <textarea class="mt-2 block h-32 w-full rounded-md border border-gray-200 bg-white px-5 py-3 text-gray-700 placeholder-gray-400 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-400 focus:ring-opacity-40 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-300 dark:placeholder-gray-600 dark:focus:border-blue-400 md:h-56" placeholder="Message"></textarea>
        </div>

        <button class="mt-4 w-full transform rounded-md bg-blue-500 px-6 py-3 text-sm font-medium capitalize tracking-wide text-white transition-colors duration-300 hover:bg-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50">get in touch</button>
        </form>
    </div>
    </section>

    <footer class="bg-white dark:bg-gray-900">
    <div class="container mx-auto px-6 py-20">
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 sm:gap-y-10 lg:grid-cols-4">
        <div class="sm:col-span-2">
            <h1 class="max-w-lg text-3xl font-semibold tracking-tight text-gray-800 dark:text-white xl:text-4xl">Subscribe our newsletter to get update.</h1>

            <div class="mx-auto mt-8 flex flex-col space-y-3 md:flex-row md:space-y-0">
            <input id="email" type="text" class="rounded-md border bg-white px-4 py-2 text-gray-700 focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300" placeholder="Email Address" />

            <button class="w-full transform rounded-lg bg-gray-800 px-6 py-2.5 text-sm font-medium tracking-wider text-white transition-colors duration-300 hover:bg-gray-700 focus:outline-none focus:ring focus:ring-gray-300 focus:ring-opacity-80 md:mx-4 md:w-auto">Subscribe</button>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Quick Link</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Home</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Who We Are</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Our Philosophy</a>
            </div>
        </div>

        <div>
            <p class="font-semibold text-gray-800 dark:text-white">Industries</p>

            <div class="mt-5 flex flex-col items-start space-y-2">
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Retail & E-Commerce</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Information Technology</a>
            <a href="#" class="text-gray-600 transition-colors duration-300 hover:text-blue-500 hover:underline dark:text-gray-300 dark:hover:text-blue-400">Finance & Insurance</a>
            </div>
        </div>
        </div>

        <hr class="my-6 border-gray-200 dark:border-gray-700 md:my-8" />

        <div class="flex items-center justify-between">
        <a href="#" class="text-2xl font-bold text-gray-800 transition-colors duration-300 hover:text-gray-700 dark:text-white dark:hover:text-gray-300">Brand</a>

        <div class="-mx-2 flex">
            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Reddit">
            <svg class="h-5 w-5 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C21.9939 17.5203 17.5203 21.9939 12 22ZM6.807 10.543C6.20862 10.5433 5.67102 10.9088 5.45054 11.465C5.23006 12.0213 5.37133 12.6558 5.807 13.066C5.92217 13.1751 6.05463 13.2643 6.199 13.33C6.18644 13.4761 6.18644 13.6229 6.199 13.769C6.199 16.009 8.814 17.831 12.028 17.831C15.242 17.831 17.858 16.009 17.858 13.769C17.8696 13.6229 17.8696 13.4761 17.858 13.33C18.4649 13.0351 18.786 12.3585 18.6305 11.7019C18.475 11.0453 17.8847 10.5844 17.21 10.593H17.157C16.7988 10.6062 16.458 10.7512 16.2 11C15.0625 10.2265 13.7252 9.79927 12.35 9.77L13 6.65L15.138 7.1C15.1931 7.60706 15.621 7.99141 16.131 7.992C16.1674 7.99196 16.2038 7.98995 16.24 7.986C16.7702 7.93278 17.1655 7.47314 17.1389 6.94094C17.1122 6.40873 16.6729 5.991 16.14 5.991C16.1022 5.99191 16.0645 5.99491 16.027 6C15.71 6.03367 15.4281 6.21641 15.268 6.492L12.82 6C12.7983 5.99535 12.7762 5.993 12.754 5.993C12.6094 5.99472 12.4851 6.09583 12.454 6.237L11.706 9.71C10.3138 9.7297 8.95795 10.157 7.806 10.939C7.53601 10.6839 7.17843 10.5422 6.807 10.543ZM12.18 16.524C12.124 16.524 12.067 16.524 12.011 16.524C11.955 16.524 11.898 16.524 11.842 16.524C11.0121 16.5208 10.2054 16.2497 9.542 15.751C9.49626 15.6958 9.47445 15.6246 9.4814 15.5533C9.48834 15.482 9.52348 15.4163 9.579 15.371C9.62737 15.3318 9.68771 15.3102 9.75 15.31C9.81233 15.31 9.87275 15.3315 9.921 15.371C10.4816 15.7818 11.159 16.0022 11.854 16C11.9027 16 11.9513 16 12 16C12.059 16 12.119 16 12.178 16C12.864 16.0011 13.5329 15.7863 14.09 15.386C14.1427 15.3322 14.2147 15.302 14.29 15.302C14.3653 15.302 14.4373 15.3322 14.49 15.386C14.5985 15.4981 14.5962 15.6767 14.485 15.786V15.746C13.8213 16.2481 13.0123 16.5208 12.18 16.523V16.524ZM14.307 14.08H14.291L14.299 14.041C13.8591 14.011 13.4994 13.6789 13.4343 13.2429C13.3691 12.8068 13.6162 12.3842 14.028 12.2269C14.4399 12.0697 14.9058 12.2202 15.1478 12.5887C15.3899 12.9572 15.3429 13.4445 15.035 13.76C14.856 13.9554 14.6059 14.0707 14.341 14.08H14.306H14.307ZM9.67 14C9.11772 14 8.67 13.5523 8.67 13C8.67 12.4477 9.11772 12 9.67 12C10.2223 12 10.67 12.4477 10.67 13C10.67 13.5523 10.2223 14 9.67 14Z"></path>
            </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Facebook">
            <svg class="h-5 w-5 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.00195 12.002C2.00312 16.9214 5.58036 21.1101 10.439 21.881V14.892H7.90195V12.002H10.442V9.80204C10.3284 8.75958 10.6845 7.72064 11.4136 6.96698C12.1427 6.21332 13.1693 5.82306 14.215 5.90204C14.9655 5.91417 15.7141 5.98101 16.455 6.10205V8.56104H15.191C14.7558 8.50405 14.3183 8.64777 14.0017 8.95171C13.6851 9.25566 13.5237 9.68693 13.563 10.124V12.002H16.334L15.891 14.893H13.563V21.881C18.8174 21.0506 22.502 16.2518 21.9475 10.9611C21.3929 5.67041 16.7932 1.73997 11.4808 2.01722C6.16831 2.29447 2.0028 6.68235 2.00195 12.002Z"></path>
            </svg>
            </a>

            <a href="#" class="mx-2 text-gray-600 transition-colors duration-300 hover:text-blue-500 dark:text-gray-300 dark:hover:text-blue-400" aria-label="Github">
            <svg class="h-5 w-5 fill-current" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12.026 2C7.13295 1.99937 2.96183 5.54799 2.17842 10.3779C1.395 15.2079 4.23061 19.893 8.87302 21.439C9.37302 21.529 9.55202 21.222 9.55202 20.958C9.55202 20.721 9.54402 20.093 9.54102 19.258C6.76602 19.858 6.18002 17.92 6.18002 17.92C5.99733 17.317 5.60459 16.7993 5.07302 16.461C4.17302 15.842 5.14202 15.856 5.14202 15.856C5.78269 15.9438 6.34657 16.3235 6.66902 16.884C6.94195 17.3803 7.40177 17.747 7.94632 17.9026C8.49087 18.0583 9.07503 17.99 9.56902 17.713C9.61544 17.207 9.84055 16.7341 10.204 16.379C7.99002 16.128 5.66202 15.272 5.66202 11.449C5.64973 10.4602 6.01691 9.5043 6.68802 8.778C6.38437 7.91731 6.42013 6.97325 6.78802 6.138C6.78802 6.138 7.62502 5.869 9.53002 7.159C11.1639 6.71101 12.8882 6.71101 14.522 7.159C16.428 5.868 17.264 6.138 17.264 6.138C17.6336 6.97286 17.6694 7.91757 17.364 8.778C18.0376 9.50423 18.4045 10.4626 18.388 11.453C18.388 15.286 16.058 16.128 13.836 16.375C14.3153 16.8651 14.5612 17.5373 14.511 18.221C14.511 19.555 14.499 20.631 14.499 20.958C14.499 21.225 14.677 21.535 15.186 21.437C19.8265 19.8884 22.6591 15.203 21.874 10.3743C21.089 5.54565 16.9181 1.99888 12.026 2Z"></path>
            </svg>
            </a>
        </div>
        </div>
    </div>
    </footer>

</main>'''
    },{
    "html":'''<!-- I've set max-w-screen-md, you may need to change it -->
    <nav class="bg-white shadow fixed max-w-screen-md z-10 mx-auto inset-x-0 top-0 flex justify-between items-center">
      
        <a href="#" class="font-extrabold m-3 uppercase inline-flex hover:text-pink-700 transition-all duration-500">
            <svg class="h-6 w-6 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path fill="#fff" d="M12 14l9-5-9-5-9 5 9 5z" />
                <path fill="#fff" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />
            </svg>
          NEED JOB
        </a>
      
        <button id="mobileMenuButton" class="p-3 focus:outline-none md:hidden" title="Open side menu">
          <!-- SVG For "x" button -->
            <svg id="mobileMenuButtonClose" class="w-6 h-6 hidden" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
          <!-- SVG For "Menu burger" button -->
            <svg id="mobileMenuButtonOpen" class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
        </button>
      
      <!-- List of nav item -->
        <div id="sideMenuHideOnMobile" class="bg-white font-semibold z-10 rounded-bl-md flex absolute top-0 right-0 transition-all duration-500 transform translate-x-0
                                              w-1/2 md:w-auto
                                              px-3 md:px-0
                                              flex-col md:flex-row
                                              -translate-y-full md:translate-y-0
                                              md:mt-1 md:items-center md:mx-1 md:uppercase">
            <a href="#" class="mx-0 sm:mx-2 my-2 border-b-2 border-transparent hover:border-pink-600 hover:text-pink-700 transition-all duration-500 py-1 sm:p-0">Project</a>
            <a href="#" class="mx-0 sm:mx-2 my-2 border-b-2 border-transparent hover:border-pink-600 hover:text-pink-700 transition-all duration-500 py-1 sm:p-0">Resource</a>
            <a href="#" class="mx-0 sm:mx-2 my-2 border-b-2 border-transparent hover:border-pink-600 hover:text-pink-700 transition-all duration-500 py-1 sm:p-0">About</a>
        </div>
      
    </nav>

    <script>
    var mobileMenuButton = document.getElementById("mobileMenuButton");
    mobileMenuButton.onclick = function() {
        document.getElementById("sideMenuHideOnMobile").classList.toggle("-translate-y-full");
        document.getElementById("sideMenuHideOnMobile").classList.toggle("mt-12");
        document.getElementById("sideMenuHideOnMobile").classList.toggle("shadow");
        document.getElementById("mobileMenuButtonClose").classList.toggle("hidden");
        document.getElementById("mobileMenuButtonOpen").classList.toggle("hidden");
    }
      // Hide element when click outside nav
    var theElementContainer = document.getElementsByTagName("nav")[0];
    document.addEventListener('click', function(event) {
        if (!theElementContainer.contains(event.target)) {
            document.getElementById("sideMenuHideOnMobile").classList.add("-translate-y-full");
            document.getElementById("sideMenuHideOnMobile").classList.remove("mt-12");
            document.getElementById("sideMenuHideOnMobile").classList.remove("shadow");
            document.getElementById("mobileMenuButtonOpen").classList.remove("hidden");
            document.getElementById("mobileMenuButtonClose").classList.add("hidden");
        }
    });
    </script>'''
    },{
    "html":'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="hero section">


    <link rel="stylesheet" href="css/tailus.css">
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400&display=swap" rel="stylesheet">
  
    <style>
        body {
            font-family : Urbanist, sans-serif;
            @apply bg-white dark:bg-gray-900
        }

        .navbar-active .hamburger div:first-child {
            @apply rotate-45 translate-y-1.5;
        }
        .navbar-active .hamburger div:last-child {
            @apply -rotate-45 -translate-y-1;
        }
        .navbar-active div:first-child div:first-child div:last-child{
            @apply block lg:flex
        }
    </style>
  </head>

  <body class="bg-white dark:bg-gray-900">
    <header>
        <input type="checkbox" name="hbr" id="hbr" class="hbr peer" hidden aria-hidden="true">
        <nav class="fixed z-20 w-full bg-white/90 dark:bg-gray-900/80 backdrop-blur navbar shadow-2xl shadow-gray-600/5 border-b border-gray-100 dark:border-gray-800 peer-checked:navbar-active dark:shadow-none">
            <div class="xl:container m-auto px-6 md:px-12 lg:px-6">
                <div class="flex flex-wrap items-center justify-between gap-6 md:py-3 md:gap-0 lg:py-5">
                    <div class="w-full items-center flex justify-between lg:w-auto">
                        <a class="relative z-10" href="#" aria-label="logo">
                            <svg class="h-9 text-[#007FEC] dark:text-[#00B1FD]" viewBox="0 0 942 272" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path class="text-blue-900 dark:text-white" d="M392.603 62.008V102.536H420.075V130.552H392.603V192.024C392.603 197.827 393.963 202.088 396.683 204.808C399.403 207.347 403.664 208.616 409.467 208.616C413.093 208.616 416.72 208.253 420.347 207.528V233.64C415.632 235.635 409.195 236.632 401.035 236.632C388.704 236.632 379.003 233.187 371.931 226.296C364.859 219.224 361.323 209.523 361.323 197.192V130.552H336.843V102.536H343.643C350.352 102.536 355.429 100.632 358.875 96.824C362.32 93.016 364.043 88.0293 364.043 81.864V62.008H392.603ZM432.359 199.096C432.359 187.853 435.986 178.877 443.239 172.168C450.674 165.277 460.375 160.925 472.343 159.112L506.343 153.944C512.871 153.037 516.135 149.864 516.135 144.424C516.135 138.44 514.05 133.635 509.879 130.008C505.709 126.2 499.453 124.296 491.111 124.296C483.133 124.296 476.786 126.563 472.071 131.096C467.357 135.448 464.637 141.16 463.911 148.232L435.079 141.704C436.349 129.736 442.061 119.581 452.215 111.24C462.37 102.717 475.245 98.456 490.839 98.456C510.061 98.456 524.205 103.08 533.271 112.328C542.519 121.576 547.143 133.453 547.143 147.96V213.784C547.143 222.488 547.687 229.56 548.775 235H519.399C518.493 232.28 518.039 226.659 518.039 218.136C509.335 232.099 495.735 239.08 477.239 239.08C463.821 239.08 452.941 235.181 444.599 227.384C436.439 219.405 432.359 209.976 432.359 199.096ZM483.223 214.328C493.015 214.328 500.903 211.699 506.887 206.44C513.053 201 516.135 192.205 516.135 180.056V174.072L481.591 179.24C469.805 181.235 463.911 187.219 463.911 197.192C463.911 201.907 465.634 205.987 469.079 209.432C472.525 212.696 477.239 214.328 483.223 214.328ZM604.325 235H573.045V102.536H604.325V235ZM574.133 70.44C570.144 66.4507 568.149 61.6453 568.149 56.024C568.149 50.4027 570.144 45.5973 574.133 41.608C578.122 37.4373 582.928 35.352 588.549 35.352C594.352 35.352 599.248 37.3467 603.237 41.336C607.226 45.3253 609.221 50.2213 609.221 56.024C609.221 61.6453 607.226 66.4507 603.237 70.44C599.248 74.4293 594.352 76.424 588.549 76.424C582.928 76.424 578.122 74.4293 574.133 70.44ZM664.341 235H632.789V38.072H664.341V235ZM778.227 220.312C775.144 226.115 770.067 230.648 762.995 233.912C756.104 237.176 748.669 238.808 740.691 238.808C725.277 238.808 713.037 233.821 703.971 223.848C695.085 213.875 690.643 201.272 690.643 186.04V102.536H722.195V180.328C722.195 189.213 724.371 196.467 728.723 202.088C733.075 207.709 739.784 210.52 748.851 210.52C757.736 210.52 764.536 207.8 769.251 202.36C774.147 196.92 776.595 189.757 776.595 180.872V102.536H808.147V210.792C808.147 218.771 808.6 226.84 809.507 235H779.315C778.589 231.011 778.227 226.115 778.227 220.312ZM825.051 199.096L852.523 191.48C853.067 197.827 855.696 203.176 860.411 207.528C865.126 211.88 871.472 214.056 879.451 214.056C885.616 214.056 890.422 212.605 893.867 209.704C897.494 206.803 899.307 203.176 899.307 198.824C899.307 191.208 894.139 186.312 883.803 184.136L864.219 179.784C852.795 177.245 844 172.531 837.835 165.64C831.67 158.749 828.587 150.589 828.587 141.16C828.587 129.555 833.302 119.581 842.731 111.24C852.16 102.717 863.675 98.456 877.275 98.456C885.979 98.456 893.686 99.7253 900.395 102.264C907.104 104.803 912.272 108.157 915.899 112.328C919.707 116.317 922.608 120.216 924.603 124.024C926.598 127.832 927.867 131.64 928.411 135.448L901.755 143.064C901.03 137.987 898.672 133.453 894.683 129.464C890.875 125.293 885.072 123.208 877.275 123.208C871.835 123.208 867.302 124.749 863.675 127.832C860.048 130.733 858.235 134.269 858.235 138.44C858.235 145.875 862.678 150.499 871.563 152.312L891.691 156.392C904.022 159.112 913.451 164.008 919.979 171.08C926.507 178.152 929.771 186.675 929.771 196.648C929.771 207.709 925.328 217.592 916.443 226.296C907.739 234.819 895.499 239.08 879.723 239.08C870.656 239.08 862.496 237.72 855.243 235C848.171 232.28 842.55 228.835 838.379 224.664C834.39 220.312 831.216 216.051 828.859 211.88C826.683 207.528 825.414 203.267 825.051 199.096Z" fill="currentColor"/>
                                <circle cx="126.5" cy="135.5" r="49" stroke="none" stroke-width="11" fill="currentColor"/>
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M157.616 38.7183C137.547 27.9866 113.297 28.3356 93.5 39.7654L60.0914 59.0538C39.6709 70.8436 27.0914 92.632 27.0914 116.212V154.788C27.0914 178.368 39.6709 200.156 60.0914 211.946L93.5 231.235C113.92 243.024 139.08 243.024 159.5 231.235L192.909 211.946C213.329 200.156 225.909 178.368 225.909 154.788V116.212C225.909 99.106 219.289 82.9431 207.857 70.8562C214.603 65.9281 219.348 58.424 220.644 49.7914C239.072 66.6422 249.909 90.6554 249.909 116.212V154.788C249.909 186.942 232.755 216.654 204.909 232.731L171.5 252.019C143.654 268.096 109.346 268.096 81.5 252.019L48.0914 232.731C20.2453 216.654 3.09137 186.942 3.09137 154.788V116.212C3.09137 84.0576 20.2453 54.3462 48.0914 38.2692L81.5 18.9808C109.138 3.02371 143.143 2.90471 170.876 18.6237C164.141 23.2603 159.27 30.4096 157.616 38.7183Z" fill="currentColor"/>
                                <circle cx="189" cy="45" r="21" fill="currentColor"/>
                            </svg>
                        </a>
                        <label for="hbr" class="peer-checked:hamburger block relative z-20 p-6 -mr-6 cursor-pointer lg:hidden">
                            <div aria-hidden="true" class="m-auto h-0.5 w-5 rounded bg-gray-900 dark:bg-gray-300 transition duration-300"></div>
                            <div aria-hidden="true" class="m-auto mt-2 h-0.5 w-5 rounded bg-gray-900 dark:bg-gray-300 transition duration-300"></div>
                        </label>
                    </div>
                    <div class="navmenu hidden w-full flex-wrap justify-end items-center mb-16 space-y-8 p-6 border border-gray-100 rounded-3xl shadow-2xl shadow-gray-300/20 bg-white dark:bg-gray-800 lg:space-y-0 lg:p-0 lg:m-0 lg:flex md:flex-nowrap lg:bg-transparent lg:w-7/12 lg:shadow-none dark:shadow-none dark:border-gray-700 lg:border-0">
                        <div class="text-gray-600 dark:text-gray-300 lg:pr-4">
                            <ul class="space-y-6 tracking-wide font-medium text-base lg:text-sm lg:flex lg:space-y-0">
                                <li>
                                    <a href="#" class="block md:px-4 transition hover:text-primary dark:hover:text-primaryLight">
                                        <span>Home</span>
                                    </a>
                                </li>
                                <li>
                                    <a href="#" class="block md:px-4 transition hover:text-primary dark:hover:text-primaryLight">
                                        <span>Portfolio</span>
                                    </a>
                                </li>
                                <li>
                                    <a href="#" class="block md:px-4 transition hover:text-primary dark:hover:text-primaryLight">
                                        <span>Services</span>
                                    </a>
                                </li>
                            </ul>
                        </div>
    
                        <div class="w-full space-y-2 border-primary/10 dark:border-gray-700 flex flex-col -ml-1 sm:flex-row lg:space-y-0 md:w-max lg:border-l">
                            <a href="#" class="relative flex h-9 ml-auto items-center justify-center sm:px-6 before:absolute before:inset-0 before:rounded-full focus:before:bg-sky-600/10 dark:focus:before:bg-sky-400/10 before:transition before:duration-300 hover:before:scale-105 active:duration-75 active:before:scale-95">
                                <span class="relative text-sm font-semibold text-primary dark:text-primaryLight">Sign Up</span>                    
                            </a>
                            <a href="#" class="relative flex h-9 ml-auto items-center justify-center sm:px-6 before:absolute before:inset-0 before:rounded-full before:bg-sky-600 dark:before:bg-sky-400 before:transition before:duration-300 hover:before:scale-105 active:duration-75 active:before:scale-95">
                                <span class="relative text-sm font-semibold text-white dark:text-gray-900">Login</span>                    
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </header>
    
    <div class="bg-white relative pt-40 pb-20 lg:pt-44 dark:bg-gray-900">
        <div class="relative xl:container m-auto px-6 md:px-12 lg:px-6">
            <h1 class="sm:mx-auto sm:w-10/12 md:w-2/3 font-black text-blue-900 text-4xl text-center sm:text-5xl md:text-6xl lg:w-auto lg:text-left xl:text-7xl dark:text-white">Run successful remote and <br class="lg:block hidden"> <span class="relative text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300">Hybrid teams</span>.</h1>
            <div class="lg:flex">
                <div class="relative mt-8 md:mt-16 space-y-8 sm:w-10/12 md:w-2/3 lg:ml-0 sm:mx-auto text-center lg:text-left lg:mr-auto lg:w-7/12">
                    <p class="sm:text-lg text-gray-700 dark:text-gray-300 lg:w-11/12">
                        DailyBot takes chat and collaboration to the next level: daily standups, team check-ins, surveys, kudos, best companion bot for your virtual watercooler, 1:1 intros, motivation tracking and more.
                    </p>
                    <span class="block font-semibold text-gray-500 dark:text-gray-400">The best companion bot for your chat app.</span>
                    <div class="grid grid-cols-3 space-x-4 md:space-x-6 md:flex md:justify-center lg:justify-start">
                        <a aria-label="add to slack" href="#" class="p-4 border border-gray-200 dark:bg-gray-800 dark:border-gray-700 rounded-full duration-300 hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-600/20 dark:hover:border-cyan-300/30">
                            <div class="flex justify-center space-x-4">
                                <img class="w-6 h-6" src="https://tailus.io/sources/blocks/tech-startup/preview/images/slack.png" alt="slack logo" loading="lazy" width="128" height="128">
                                <span class="hidden font-medium md:block dark:text-white">Slack</span>
                            </div>
                        </a>    
                        <a aria-label="add to chat" href="#" class="p-4 border border-gray-200 dark:bg-gray-800  dark:border-gray-700 rounded-full duration-300 hover:border-green-400 hover:shadow-lg hover:shadow-lime-600/20 dark:hover:border-green-300/30">
                            <div class="flex justify-center space-x-4">
                                <img class="w-6 h-6" src="https://tailus.io/sources/blocks/tech-startup/preview/images/chat.png" alt="chat logo" loading="lazy" width="128" height="128">
                                <span class="hidden font-medium md:block dark:text-white">Google Chat</span>
                            </div>
                        </a>   
                        <a aria-label="add to zoom" href="#" class="p-4 border border-gray-200 dark:bg-gray-800  dark:border-gray-700 rounded-full duration-300 hover:border-blue-400 hover:shadow-lg hover:shadow-blue-600/20 dark:hover:border-blue-300/30">
                            <div class="flex justify-center space-x-4">
                                <img class="w-6 h-6" src="https://tailus.io/sources/blocks/tech-startup/preview/images/zoom.png" alt="chat logo" loading="lazy" width="128" height="128">
                                <span class="hidden font-medium md:block dark:text-white">Zoom</span>
                            </div>
                        </a>    
                    </div>

                    <div class="dark:text-gray-300">
                        🔥🌟 
                        <span>Other integrations :</span> 
                        <a href="#" class="font-semibold text-gray-700 dark:text-gray-200">Discord,</a>
                        <a href="#" class="font-semibold text-gray-700 dark:text-gray-200">Telegram</a>
                    </div>

                    <div class="pt-12 flex gap-6 lg:gap-12 justify-between grayscale lg:w-2/3">
                        <img src="https://tailus.io/sources/blocks/tech-startup/preview/images/clients/airbnb.svg" class="h-8 sm:h-10 w-auto lg:h-12" alt="" />
                        <img src="https://tailus.io/sources/blocks/tech-startup/preview/images/clients/ge.svg" class="h-8 sm:h-10 w-auto lg:h-12" alt="" />
                        <img src="https://tailus.io/sources/blocks/tech-startup/preview/images/clients/coty.svg" class="h-8 sm:h-10 w-auto lg:h-12" alt="" />
                        <img src="https://tailus.io/sources/blocks/tech-startup/preview/images/clients/microsoft.svg" class="h-8 sm:h-10 w-auto lg:h-12" alt="" />
                    </div>
                </div>
                <div class="mt-12 md:mt-0 lg:absolute -right-10 lg:w-7/12">
                    <div class="relative w-full">
                        <div aria-hidden="true" class="absolute scale-75 md:scale-110 inset-0 m-auto w-full h-full md:w-96 md:h-96 rounded-full rotate-45 bg-gradient-to-r from-sky-500 to-cyan-300 blur-3xl"></div>
                        <img src="https://tailus.io/sources/blocks/tech-startup/preview/images/globalization-cuate.svg" class="relative w-full" alt="wath illustration" loading="lazy" width="320" height="280">
                    </div>
                </div>
            </div>
        </div>
    </div>
  </body>
</html>'''
    },
    {
    "html":'''<link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css"
    />

<!-- This is an example component -->
<div
      class="bg-grayDark"
    x-data="{ atTop: true }"
    x-on:scroll.window="atTop =( window.pageYOffset > 10) ? false : true "
     >
    <!-- Navbar -->
    <div
      class="w-full text-gray-700 bg-white h-16 fixed top-0 animated z-40"
      x-bind:class='{ "bg-black shadow-lg": !atTop }'
    >
      <div
        x-data="{ open: false }"
        class="flex flex-col max-w-screen-xl px-2 mx-auto md:items-center md:justify-between md:flex-row"
      >
        <div class="p-4 flex flex-row items-center justify-between">
          <a
            href="home.html"
            class="tracking-widest rounded-lg focus:outline-none focus:shadow-outline"
          >
            <svg class="w-8 h-8 text-purple-600" width="54" height="54" viewBox="0 0 54 54" xmlns="http://www.w3.org/2000/svg">
          <title>TailwindCSS</title>
          <path fill="currentColor" d="M13.5 22.1c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05zM0 38.3c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05z"></path>
        </svg>
          </a>
          <!-- Button Mobile Nav -->
          <button
            class="md:hidden rounded-lg focus:outline-none focus:shadow-outline"
            @click="open = !open"
          >
            <span class="text-lg text-primary"
              ><i class="fas fa-bell"></i
            ></span>
          </button>
          <!-- End Button Mobile Nav -->
        </div>
        <!-- Navbar Mobile -->
        <nav
          :class="{'flex': open, 'hidden': !open}"
          class="flex-col flex-grow pb-4 hidden bg-white shadow-lg rounded-b"
        >
          <a
            class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
            href="#"
            >Notifikasi 1</a
          >
          <a
          class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
          href="#"
          >Notifikasi 1</a
        >
        <a
        class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
        href="#"
        >Notifikasi 1</a
      >
      <a
      class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
      href="#"
      >Notifikasi 1</a
    >
        </nav>
        <!-- End Navbar Mobile -->
        <nav
          class="flex-col flex-grow pb-4 md:pb-0 hidden md:flex md:justify-end md:flex-row bg-white"
        >
          <a
            class="flex items-center px-3 py-1 mt-2 text-lg font-semibold text-primary rounded-lg md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
            href="#"
          >
            <i class="fas fa-envelope"></i>
          </a>
          <div
            @click.away="open = false"
            class="relative"
            x-data="{ open: false }"
          >
            <button
              @click="open = !open"
              class="flex flex-row items-center w-full px-3 py-1 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg md:w-auto md:mt-0 md:ml-2 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
            >
              <span class="text-lg text-primary"
                ><i class="fas fa-bell"></i
              ></span>
            </button>
            <div
              x-show="open"
              x-transition:enter="transition ease-out duration-100"
              x-transition:enter-start="transform opacity-0 scale-95"
              x-transition:enter-end="transform opacity-100 scale-100"
              x-transition:leave="transition ease-in duration-75"
              x-transition:leave-start="transform opacity-100 scale-100"
              x-transition:leave-end="transform opacity-0 scale-95"
              class="absolute right-0 w-full mt-2 origin-top-right rounded-md shadow-lg md:w-48"
            >
              <div class="px-2 py-2 bg-white rounded-md shadow">
                <a
                  class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
                  href="#"
                  >Notifikasi 1</a
                >
                <a
                  class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
                  href="#"
                  >Notifikasi #2</a
                >
                <a
                  class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
                  href="#"
                  >Notifikasi #3</a
                >
              </div>
            </div>
          </div>
          <div
            @click.away="open = false"
            class="relative"
            x-data="{ open: false }"
          >
            <button
              @click="open = !open"
              class="flex flex-row items-center w-full px-1 py-1 mt-2 text-sm font-semibold text-left bg-transparent rounded-full md:w-auto md:mt-0 md:ml-2 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
            >
              <img src="https://randomuser.me/api/portraits/men/12.jpg" class="w-auto h-6 rounded-full" alt="" />
            </button>
            <div
              x-show="open"
              x-transition:enter="transition ease-out duration-100"
              x-transition:enter-start="transform opacity-0 scale-95"
              x-transition:enter-end="transform opacity-100 scale-100"
              x-transition:leave="transition ease-in duration-75"
              x-transition:leave-start="transform opacity-100 scale-100"
              x-transition:leave-end="transform opacity-0 scale-95"
              class="absolute right-0 w-full mt-2 origin-top-right rounded-md shadow-lg md:w-48"
            >
              <div class="px-2 py-2 bg-white rounded-md shadow">
                <a
                  class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
                  href="forum.html"
                  >Forum</a
                >
                <a
                  class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
                  href="chat.html"
                  >Chat</a
                >
                <a
                  class="block px-4 py-2 mt-2  bg-transparent rounded-lg  text-sm font-semibold md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline"
                  href="#"
                  >Link #3</a
                >
              </div>
            </div>
          </div>
        </nav>
      </div>
    </div>
    <!-- End Navbar -->
  <div class="w-full  md:pl-4 lg:pl-10 md:pr-4 flex self-start flex-col mt-20">
    <div class="w-full rounded overflow-hidden shadow-lg bg-white flex flex-col p-6 md:py-8 lg:py-12 xl:py-16 md:px-8 lg:px-12 xl:px-20">
      <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
    </div>
  </div>
</div>

<script
    src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js"
    defer
  ></script>'''
    },{
    "html":'''<!-- This is an example component -->
<body x-data="imageGallery()" 
      x-init="fetch('https://pixabay.com/api/?key=15819227-ef2d84d1681b9442aaa9755b8&q=woman+girl+food&image_type=all&per_page=52&')
      .then(response => response.json())
      .then(response => { images = response.hits })"
      class="bg-white">

<div class="main">
    <div class="px-4 sm:px-8 lg:px-16 xl:px-20 mx-auto">

        <!-- hero -->
        <div class="hero">
            <!-- hero headline -->
            <div class="hero-headline flex flex-col items-center justify-center pt-24 text-center">
                <h1 class=" font-bold text-3xl text-gray-900">Stunning free images & royalty free stock</h1>
                <p class=" font-base text-base text-gray-600">high quality stock images and videos shared by our talented community.</p>
            </div>

            <!-- image search box -->
            <div class="box pt-6">
                <div class="box-wrapper">

                    <div class=" bg-white rounded flex items-center w-full p-3 shadow-sm border border-gray-200">
                      <button @click="getImages()" class="outline-none focus:outline-none"><svg class=" w-5 text-gray-600 h-5 cursor-pointer" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" stroke="currentColor" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg></button>
                      <input type="search" name="" id="" @keydown.enter="getImages()" placeholder="search for images" x-model="q" class="w-full pl-4 text-sm outline-none focus:outline-none bg-transparent">
                      <div class="select">
                        <select name="" id="" x-model="image_type" class="text-sm outline-none focus:outline-none bg-transparent">
                          <option value="all" selected>All</option>
                          <option value="photo">Photo</option>
                          <option value="illustration">Illustration</option>
                          <option value="vector">Vector</option>
                         </select>
                      </div>
                    </div>
                  
                </div>
            </div>

            <section id="photos" class="my-5 grid grid-cols-1 md:grid-cols-4 gap-4">
                <template x-for="image in images" :key="image.id">
                  <a :href="image.largeImageURL" class="hover:opacity-75 " target="_new"><img class="w-full h-64 object-cover" :src="image.largeImageURL" :alt="image.tags" /></a>
                </template>
              </section>

        </div>

        <footer class="p-5 text-sm text-gray-600 text-center inline-flex items-center">
          <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="heart" class="svg-inline--fa fa-heart fa-w-16 text-red-600 w-4 h-4 mr-4 align-middle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"></path></svg>
          <span>Made by <a href="https://tailwindcss.com/" target="_new" class="text-teal-600 font-semibold">tailwindcss</a> & <a href="https://github.com/alpinejs/alpine" target="_new" class="text-teal-600 font-semibold">alpinejs</a></span>
        </footer>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.3.5/dist/alpine.min.js" defer></script>
<script>
    function imageGallery() {
        return {
          images: [],
          api_key : "15819227-ef2d84d1681b9442aaa9755b8",
          q: "",
          image_type: "",
          page: "",
          per_page: 52,
          getImages: async function() {
            console.log("params", this.q, this.image_type);  
            const response = await fetch(
              `https://pixabay.com/api/?key=${this.api_key}&q=${
                this.q
              }&image_type=${this.image_type}&per_page=${this.per_page}&page=${this.page}`
            );
            const data = await response.json();
            this.images = data.hits;
          }
        };
      }
</script>'''
    },{
    "html":'''<!-- This is an example component -->
<div class='relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12'>
  <div class="flex items-center justify-between border-b bg-blue-400 p-3">
    <div class="flex items-center space-x-2 rounded bg-gray-100 py-1 px-2 text-slate-500 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-4 w-4">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 12h-15m0 0l6.75 6.75M4.5 12l6.75-6.75" />
      </svg>
      <span>Back</span>
    </div>
    <div class="text-lg font-bold text-gray-100">filename.pdf</div>
    <div class="flex items-center space-x-5 text-gray-100">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
        <path fill-rule="evenodd" d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z" clip-rule="evenodd" />
      </svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
        <path fill-rule="evenodd" d="M5.625 1.5H9a3.75 3.75 0 013.75 3.75v1.875c0 1.036.84 1.875 1.875 1.875H16.5a3.75 3.75 0 013.75 3.75v7.875c0 1.035-.84 1.875-1.875 1.875H5.625a1.875 1.875 0 01-1.875-1.875V3.375c0-1.036.84-1.875 1.875-1.875zm6.905 9.97a.75.75 0 00-1.06 0l-3 3a.75.75 0 101.06 1.06l1.72-1.72V18a.75.75 0 001.5 0v-4.19l1.72 1.72a.75.75 0 101.06-1.06l-3-3z" clip-rule="evenodd" />
        <path d="M14.25 5.25a5.23 5.23 0 00-1.279-3.434 9.768 9.768 0 016.963 6.963A5.23 5.23 0 0016.5 7.5h-1.875a.375.375 0 01-.375-.375V5.25z" />
      </svg>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
        <path fill-rule="evenodd" d="M5.625 1.5H9a3.75 3.75 0 013.75 3.75v1.875c0 1.036.84 1.875 1.875 1.875H16.5a3.75 3.75 0 013.75 3.75v7.875c0 1.035-.84 1.875-1.875 1.875H5.625a1.875 1.875 0 01-1.875-1.875V3.375c0-1.036.84-1.875 1.875-1.875zm5.845 17.03a.75.75 0 001.06 0l3-3a.75.75 0 10-1.06-1.06l-1.72 1.72V12a.75.75 0 00-1.5 0v4.19l-1.72-1.72a.75.75 0 00-1.06 1.06l3 3z" clip-rule="evenodd" />
        <path d="M14.25 5.25a5.23 5.23 0 00-1.279-3.434 9.768 9.768 0 016.963 6.963A5.23 5.23 0 0016.5 7.5h-1.875a.375.375 0 01-.375-.375V5.25z" />
      </svg>
    </div>
  </div>
</div>'''
    }
]
Carousel=[
    {
    "html":'''<head>
<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.4.1.min.js"></script>
  <script>
    var cont=0;
function loopSlider(){
  var xx= setInterval(function(){
        switch(cont)
        {
        case 0:{
            $("#slider-1").fadeOut(400);
            $("#slider-2").delay(400).fadeIn(400);
            $("#sButton1").removeClass("bg-purple-800");
            $("#sButton2").addClass("bg-purple-800");
        cont=1;
        
        break;
        }
        case 1:
        {
        
            $("#slider-2").fadeOut(400);
            $("#slider-1").delay(400).fadeIn(400);
            $("#sButton2").removeClass("bg-purple-800");
            $("#sButton1").addClass("bg-purple-800");
           
        cont=0;
        
        break;
        }
        
        
        }},8000);

}

function reinitLoop(time){
clearInterval(xx);
setTimeout(loopSlider(),time);
}



function sliderButton1(){

    $("#slider-2").fadeOut(400);
    $("#slider-1").delay(400).fadeIn(400);
    $("#sButton2").removeClass("bg-purple-800");
    $("#sButton1").addClass("bg-purple-800");
    reinitLoop(4000);
    cont=0
    
    }
    
    function sliderButton2(){
    $("#slider-1").fadeOut(400);
    $("#slider-2").delay(400).fadeIn(400);
    $("#sButton1").removeClass("bg-purple-800");
    $("#sButton2").addClass("bg-purple-800");
    reinitLoop(4000);
    cont=1
    
    }

    $(window).ready(function(){
        $("#slider-2").hide();
        $("#sButton1").addClass("bg-purple-800");
        

        loopSlider();
     
        
    
    
    
    
    });

  
  </script>
</head>

<body>
  <div class="sliderAx h-auto">
      <div id="slider-1" class="container mx-auto">
        <div class="bg-cover bg-center  h-auto text-white py-24 px-10 object-fill" style="background-image: url(https://images.unsplash.com/photo-1544427920-c49ccfb85579?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1422&q=80)">
       <div class="md:w-1/2">
        <p class="font-bold text-sm uppercase">Services</p>
        <p class="text-3xl font-bold">Hello world</p>
        <p class="text-2xl mb-10 leading-none">Carousel with TailwindCSS and jQuery</p>
        <a href="#" class="bg-purple-800 py-4 px-8 text-white font-bold uppercase text-xs rounded hover:bg-gray-200 hover:text-gray-800">Contact us</a>
        </div>  
    </div> <!-- container -->
      <br>
      </div>

      <div id="slider-2" class="container mx-auto">
        <div class="bg-cover bg-top  h-auto text-white py-24 px-10 object-fill" style="background-image: url(https://images.unsplash.com/photo-1544144433-d50aff500b91?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)">
       
  <p class="font-bold text-sm uppercase">Services</p>
        <p class="text-3xl font-bold">Hello world</p>
        <p class="text-2xl mb-10 leading-none">Carousel with TailwindCSS and jQuery</p>
        <a href="#" class="bg-purple-800 py-4 px-8 text-white font-bold uppercase text-xs rounded hover:bg-gray-200 hover:text-gray-800">Contact us</a>
         
    </div> <!-- container -->
      <br>
      </div>
    </div>
 <div  class="flex justify-between w-12 mx-auto pb-2">
        <button id="sButton1" onclick="sliderButton1()" class="bg-purple-400 rounded-full w-4 pb-2 " ></button>
    <button id="sButton2" onclick="sliderButton2() " class="bg-purple-400 rounded-full w-4 p-2"></button>
  </div>

</body>'''
    },{
    "html":'''<!-- This is an example component -->
<div class="max-w-2xl mx-auto">

	<div id="default-carousel" class="relative" data-carousel="static">
        <!-- Carousel wrapper -->
        <div class="overflow-hidden relative h-56 rounded-lg sm:h-64 xl:h-80 2xl:h-96">
            <!-- Item 1 -->
            <div class="hidden duration-700 ease-in-out" data-carousel-item>
                <span class="absolute top-1/2 left-1/2 text-2xl font-semibold text-white -translate-x-1/2 -translate-y-1/2 sm:text-3xl dark:text-gray-800">First Slide</span>
                <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" class="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2" alt="...">
            </div>
            <!-- Item 2 -->
            <div class="hidden duration-700 ease-in-out" data-carousel-item>
                <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" class="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2" alt="...">
            </div>
            <!-- Item 3 -->
            <div class="hidden duration-700 ease-in-out" data-carousel-item>
                <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" class="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2" alt="...">
            </div>
        </div>
        <!-- Slider indicators -->
        <div class="flex absolute bottom-5 left-1/2 z-30 space-x-3 -translate-x-1/2">
            <button type="button" class="w-3 h-3 rounded-full" aria-current="false" aria-label="Slide 1" data-carousel-slide-to="0"></button>
            <button type="button" class="w-3 h-3 rounded-full" aria-current="false" aria-label="Slide 2" data-carousel-slide-to="1"></button>
            <button type="button" class="w-3 h-3 rounded-full" aria-current="false" aria-label="Slide 3" data-carousel-slide-to="2"></button>
        </div>
        <!-- Slider controls -->
        <button type="button" class="flex absolute top-0 left-0 z-30 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-prev>
            <span class="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                <svg class="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                <span class="hidden">Previous</span>
            </span>
        </button>
        <button type="button" class="flex absolute top-0 right-0 z-30 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-next>
            <span class="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                <svg class="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                <span class="hidden">Next</span>
            </span>
        </button>
    </div>

	<p class="mt-5">This carousel slider component is part of a larger, open-source library of Tailwind CSS components. Learn
		more
		by going to the official <a class="text-blue-600 hover:underline"
			href="https://flowbite.com/docs/getting-started/introduction/" target="_blank">Flowbite Documentation</a>.
	</p>
    <script src="https://unpkg.com/flowbite@1.4.0/dist/flowbite.js"></script>
</div>'''
    },{
    "html":'''<script defer src="https://unpkg.com/alpinejs@3.2.3/dist/cdn.min.js"></script>

<article x-data="slider" class="relative w-full flex flex-shrink-0 overflow-hidden shadow-2xl">
    <div class="rounded-full bg-gray-600 text-white absolute top-5 right-5 text-sm px-2 text-center z-10">
        <span x-text="currentIndex"></span>/
        <span x-text="images.length"></span>
    </div>

    <template x-for="(image, index) in images">
        <figure class="h-96" x-show="currentIndex == index + 1" x-transition:enter="transition transform duration-300"
        x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100"
        x-transition:leave="transition transform duration-300" x-transition:leave-start="opacity-100"
        x-transition:leave-end="opacity-0">
        <img :src="image" alt="Image" class="absolute inset-0 z-10 h-full w-full object-cover opacity-70" />
        <figcaption class="absolute inset-x-0 bottom-1 z-20 w-96 mx-auto p-4 font-light text-sm text-center tracking-widest leading-snug bg-gray-300 bg-opacity-25">
            Any kind of content here!
            Primum in nostrane potestate est, quid meminerimus? Nulla erit controversia. Vestri haec verecundius, illi fortasse constantius. 
        </figcaption>
        </figure>
    </template>

    <button @click="back()"
        class="absolute left-14 top-1/2 -translate-y-1/2 w-11 h-11 flex justify-center items-center rounded-full shadow-md z-10 bg-gray-100 hover:bg-gray-200">
        <svg class=" w-8 h-8 font-bold transition duration-500 ease-in-out transform motion-reduce:transform-none text-gray-500 hover:text-gray-600 hover:-translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7">
            </path>
        </svg>
    </button>

    <button @click="next()"
    class="absolute right-14 top-1/2 translate-y-1/2 w-11 h-11 flex justify-center items-center rounded-full shadow-md z-10 bg-gray-100 hover:bg-gray-200">
        <svg class=" w-8 h-8 font-bold transition duration-500 ease-in-out transform motion-reduce:transform-none text-gray-500 hover:text-gray-600 hover:translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path>
        </svg>
    </button>
</article>

<script>
    document.addEventListener('alpine:init', () => {
        Alpine.data('slider', () => ({
            currentIndex: 1,
            images: [
                'https://source.unsplash.com/1600x900/?beach',
                'https://source.unsplash.com/1600x900/?cat',
                'https://source.unsplash.com/1600x900/?dog',
                'https://source.unsplash.com/1600x900/?lego',
                'https://source.unsplash.com/1600x900/?textures&patterns'
            ],
            back() {
                if (this.currentIndex > 1) {
                    this.currentIndex = this.currentIndex - 1;
                }
            },
            next() {
                if (this.currentIndex < this.images.length) {
                    this.currentIndex = this.currentIndex + 1;
                } else if (this.currentIndex <= this.images.length){
                    this.currentIndex = this.images.length - this.currentIndex + 1
                }
            },
        }))
    })
</script>'''
    }
]
Checkbox =[
    {
    "html":'''<!-- This is an example component -->
<div class="max-w-lg mx-auto">
    
    <fieldset class="mb-5">
        <legend class="sr-only">Checkbox variants</legend>

        <div class="flex items-center items-start mb-4">
            <input id="checkbox-1" aria-describedby="checkbox-1" type="checkbox" class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded" checked="">
            <label for="checkbox-1" class="text-sm ml-3 font-medium text-gray-900">I agree to the <a href="#" class="text-blue-600 hover:underline">terms and conditions</a></label>
        </div>

        <div class="flex items-start items-center mb-4">
            <input id="checkbox-2" aria-describedby="checkbox-2" type="checkbox" class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded">
            <label for="checkbox-2" class="text-sm ml-3 font-medium text-gray-900">I want to get promotional offers</label>
        </div>

        <div class="flex items-start items-center mb-4">
            <input id="checkbox-3" aria-describedby="checkbox-3" type="checkbox" class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded">
            <label for="checkbox-3" class="text-sm ml-3 font-medium text-gray-900">I am 18 years or older</label>
        </div>
        
        <div class="flex items-start mb-4">
            <div class="flex items-center h-5">
            <input id="shipping-2" aria-describedby="shipping-2" type="checkbox" class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded">
            </div>
            <div class="text-sm ml-3">
            <label for="shipping-2" class="font-medium text-gray-900">Free shipping via Flowbite</label>
            <div class="text-gray-500"><span class="font-normal text-xs">For orders shipped from Flowbite from <span class="font-medium">€ 25</span> in books or <span>€ 29</span> on other categories</span></div>
            </div>
        </div>

        <div class="flex items-start items-center">
            <input id="international-shipping-disabled" aria-describedby="international-shipping-disabled" type="checkbox" class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded" disabled="">
            <label for="international-shipping-disabled" class="text-sm ml-3 font-medium text-gray-400">Eligible for international shipping (disabled)</label>
        </div>
    </fieldset>

    <p class="mt-5">This checkbox element is part of a larger, open-source library of Tailwind CSS components. Learn more by going to the official <a class="text-blue-600 hover:underline" href="#" target="_blank">Flowbite Documentation</a>.</p>
</div>

<script src="https://unpkg.com/@themesberg/flowbite@latest/dist/flowbite.bundle.js"></script>'''
    },{
    "html":'''<div class="flex items-center justify-center">
	<input
        type="checkbox"
        class="appearance-none w-9 focus:outline-none checked:bg-blue-300 h-5 bg-gray-300 rounded-full before:inline-block before:rounded-full before:bg-blue-500 before:h-4 before:w-4 checked:before:translate-x-full shadow-inner transition-all duration-300 before:ml-0.5"
    />
</div>'''
    },{
    "html":'''<div class="bg-white dark:bg-gray-900">
            <div class="container px-6 py-8 mx-auto">
                <p class="text-xl text-center text-gray-500 dark:text-gray-300">
                    Choose your plan
                </p>

                <h1 class="mt-4 text-3xl font-semibold text-center text-gray-800 capitalize lg:text-4xl dark:text-white">Pricing Plan</h1>
            
                
                <div class="mt-6 space-y-8 xl:mt-12">
                    <div class="flex items-center justify-between max-w-2xl px-8 py-4 mx-auto border cursor-pointer rounded-xl dark:border-gray-700">
                        <div class="flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-400 sm:h-9 sm:w-9" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                            </svg>

                            <div class="flex flex-col items-center mx-5 space-y-1">
                                <h2 class="text-lg font-medium text-gray-700 sm:text-2xl dark:text-gray-200">Basic</h2>
                                <div class="px-2 text-xs text-blue-500 bg-gray-100 rounded-full sm:px-4 sm:py-1 dark:bg-gray-700 ">
                                    Save 20%
                                </div>
                            </div>
                        </div>
                        
                        <h2 class="text-2xl font-semibold text-gray-500 sm:text-4xl dark:text-gray-300">$49 <span class="text-base font-medium">/Month</span></h2>
                    </div>

                    <div class="flex items-center justify-between max-w-2xl px-8 py-4 mx-auto border border-blue-500 cursor-pointer rounded-xl">
                        <div class="flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-blue-600 sm:h-9 sm:w-9" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                            </svg>

                            <div class="flex flex-col items-center mx-5 space-y-1">
                                <h2 class="text-lg font-medium text-gray-700 sm:text-2xl dark:text-gray-200">Popular</h2>
                                <div class="px-2 text-xs text-blue-500 bg-gray-100 rounded-full sm:px-4 sm:py-1 dark:bg-gray-700 ">
                                    Save 20%
                                </div>
                            </div>
                        </div>
                        
                        <h2 class="text-2xl font-semibold text-blue-600 sm:text-4xl">$99 <span class="text-base font-medium">/Month</span></h2>
                    </div>

                    <div class="flex items-center justify-between max-w-2xl px-8 py-4 mx-auto border cursor-pointer rounded-xl dark:border-gray-700">
                        <div class="flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-400 sm:h-9 sm:w-9" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                            </svg>

                            <div class="flex flex-col items-center mx-5 space-y-1">
                                <h2 class="text-lg font-medium text-gray-700 sm:text-2xl dark:text-gray-200">Enterprise</h2>
                                <div class="px-2 text-xs text-blue-500 bg-gray-100 rounded-full sm:px-4 sm:py-1 dark:bg-gray-700 ">
                                    Save 20%
                                </div>
                            </div>
                        </div>
                        
                        <h2 class="text-2xl font-semibold text-gray-500 sm:text-4xl dark:text-gray-300">$149 <span class="text-base font-medium">/Month</span></h2>
                    </div>

                    <div class="flex justify-center">
                        <button class="px-8 py-2 tracking-wide text-white capitalize transition-colors duration-200 transform bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:bg-blue-500 focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                            Choose Plan
                        </button>
                    </div>
                </div>
            </div>
        </div>'''
    },{
    "html":'''<!-- This is an example component -->
<div class="max-w-lg mx-auto">
    
    <form>
        <div class="mb-6">
            <label for="email" class="text-sm font-medium text-gray-900 block mb-2">Your email</label>
            <input type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="name@flowbite.com" required="">
        </div>
        <div class="mb-6">
            <label for="password" class="text-sm font-medium text-gray-900 block mb-2">Your password</label>
            <input type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" required="">
        </div>
        <div class="flex items-start mb-6">
            <div class="flex items-center h-5">
            <input id="remember" aria-describedby="remember" type="checkbox" class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded" required="">
            </div>
            <div class="text-sm ml-3">
            <label for="remember" class="font-medium text-gray-900">Remember me</label>
            </div>
        </div>
        <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Submit</button>
    </form>

    <p class="mt-5">This form element is part of a larger, open-source library of Tailwind CSS components. Learn more by going to the official <a class="text-blue-600 hover:underline" href="#" target="_blank">Flowbite Documentation</a>.</p>
</div>

<script src="https://unpkg.com/@themesberg/flowbite@latest/dist/flowbite.bundle.js"></script>'''
    },{
    "html":'''<div class='flex flex-col gap-6'>
	<!-- 1 -->
	<div class='flex flex-row'>
		<input type="checkbox" id="cb1" value="cb1"
        class='
            appearance-none h-6 w-6 bg-gray-400 rounded-full 
            checked:bg-green-300 checked:scale-75
            transition-all duration-200 peer
        '
    />
		<div class='h-6 w-6 absolute rounded-full pointer-events-none
        peer-checked:border-green-300 peer-checked:border-2
        '>
		</div>
		<label for='cb1' class='flex flex-col justify-center px-2 peer-checked:text-green-400  select-none'>Checkbox 1</label>
	</div>

	<!-- 2 -->

	<div class='flex flex-row'>
		<input type="checkbox" id="cb2" value="cb2"
        class='
            appearance-none h-6 w-6 bg-gray-400 rounded-full 
            checked:scale-150 checked:opacity-0
            transition-all duration-300 peer
        '
    />
		<div class='h-6 w-6 absolute rounded-full transition-all duration-300 transparent
        peer-checked:bg-green-300'>
		</div>
		<label for='cb2' class='flex flex-col justify-center px-2 peer-checked:text-green-400  select-none'>Checkbox 2</label>
	</div>

	<!-- 3 -->

	<div class='flex flex-row justify-center bg-gray-800 p-1'>
		<input type="checkbox" id="cb3" value="cb3"
        class='
            appearance-none h-6 w-2 bg-gray-400 
            checked:bg-yellow-300 checked:shadow-[0_0_5px_yellow]
            transition-all duration-300 peer
            ml-1
        '
    />
		<label for='cb3' class='flex flex-col justify-center px-2 peer-checked:text-yellow-300 select-none text-white'>Checkbox 3</label>
	</div>

	<!-- 4 -->

	<div class='flex flex-col justify-between bg-gray-800 '>
		<input type="checkbox" id="cb4" value="cb4"
        class='
            appearance-none h-1 w-full bg-gray-400 
            checked:bg-yellow-300 checked:shadow-[0_0px_5px_yellow]
            transition-all duration-300 peer
        '
    />
		<label for='cb4' class='p-1 flex flex-row justify-center px-2 peer-checked:text-yellow-300 select-none text-white'>Checkbox 4</label>
	</div>

	<!-- 5 -->

	<div class='flex flex-col justify-between bg-gray-800 relative
    '>
		<input type="checkbox" id="cb5" value="cb5"
        class='
            appearance-none peer
        '
    />
		<label for='cb5' class='p-1 flex flex-row justify-center px-2 select-none text-white peer-checked:text-green-300'>Checkbox 5</label>
		<div class='absolute w-full h-full peer-checked:shadow-[-4px_4px_0px_rgb(134,239,172)] 
        pointer-events-none transition-all duration-300'></div>
	</div>
</div>

<script>
	const childs = document.querySelectorAll('input');
    for(let i =0;i<childs.length;i++){
        window.setTimeout(function(){
            childs[i].checked = true; 
        },(i+1)*500);
    }
</script>'''
    },{
    "html":'''<div class='flex flex-col gap-6'>
	<!-- 1 -->
	<div class='flex flex-row'>
		<input type="checkbox" id="cb1" value="cb1"
        class='
            appearance-none h-6 w-6 bg-gray-400 rounded-full 
            checked:bg-green-300 checked:scale-75
            transition-all duration-200 peer
        '
    />
		<div class='h-6 w-6 absolute rounded-full pointer-events-none
        peer-checked:border-green-300 peer-checked:border-2
        '>
		</div>
		<label for='cb1' class='flex flex-col justify-center px-2 peer-checked:text-green-400  select-none'>Checkbox 1</label>
	</div>

	<!-- 2 -->

	<div class='flex flex-row'>
		<input type="checkbox" id="cb2" value="cb2"
        class='
            appearance-none h-6 w-6 bg-gray-400 rounded-full 
            checked:scale-150 checked:opacity-0
            transition-all duration-300 peer
        '
    />
		<div class='h-6 w-6 absolute rounded-full transition-all duration-300 transparent
        peer-checked:bg-green-300'>
		</div>
		<label for='cb2' class='flex flex-col justify-center px-2 peer-checked:text-green-400  select-none'>Checkbox 2</label>
	</div>

	<!-- 3 -->

	<div class='flex flex-row justify-center bg-gray-800 p-1'>
		<input type="checkbox" id="cb3" value="cb3"
        class='
            appearance-none h-6 w-2 bg-gray-400 
            checked:bg-yellow-300 checked:shadow-[0_0_5px_yellow]
            transition-all duration-300 peer
            ml-1
        '
    />
		<label for='cb3' class='flex flex-col justify-center px-2 peer-checked:text-yellow-300 select-none text-white'>Checkbox 3</label>
	</div>

	<!-- 4 -->

	<div class='flex flex-col justify-between bg-gray-800 '>
		<input type="checkbox" id="cb4" value="cb4"
        class='
            appearance-none h-1 w-full bg-gray-400 
            checked:bg-yellow-300 checked:shadow-[0_0px_5px_yellow]
            transition-all duration-300 peer
        '
    />
		<label for='cb4' class='p-1 flex flex-row justify-center px-2 peer-checked:text-yellow-300 select-none text-white'>Checkbox 4</label>
	</div>

	<!-- 5 -->

	<div class='flex flex-col justify-between bg-gray-800 relative
    '>
		<input type="checkbox" id="cb5" value="cb5"
        class='
            appearance-none peer
        '
    />
		<label for='cb5' class='p-1 flex flex-row justify-center px-2 select-none text-white peer-checked:text-green-300'>Checkbox 5</label>
		<div class='absolute w-full h-full peer-checked:shadow-[-4px_4px_0px_rgb(134,239,172)] 
        pointer-events-none transition-all duration-300'></div>
	</div>
</div>

<script>
	const childs = document.querySelectorAll('input');
    for(let i =0;i<childs.length;i++){
        window.setTimeout(function(){
            childs[i].checked = true; 
        },(i+1)*500);
    }
</script>'''
    },{
    "html":'''<div class='flex flex-col gap-6'>
	<!-- 1 -->
	<div class='flex flex-row'>
		<input type="checkbox" id="cb1" value="cb1"
        class='
            appearance-none h-6 w-6 bg-gray-400 rounded-full 
            checked:bg-green-300 checked:scale-75
            transition-all duration-200 peer
        '
    />
		<div class='h-6 w-6 absolute rounded-full pointer-events-none
        peer-checked:border-green-300 peer-checked:border-2
        '>
		</div>
		<label for='cb1' class='flex flex-col justify-center px-2 peer-checked:text-green-400  select-none'>Checkbox 1</label>
	</div>

	<!-- 2 -->

	<div class='flex flex-row'>
		<input type="checkbox" id="cb2" value="cb2"
        class='
            appearance-none h-6 w-6 bg-gray-400 rounded-full 
            checked:scale-150 checked:opacity-0
            transition-all duration-300 peer
        '
    />
		<div class='h-6 w-6 absolute rounded-full transition-all duration-300 transparent
        peer-checked:bg-green-300'>
		</div>
		<label for='cb2' class='flex flex-col justify-center px-2 peer-checked:text-green-400  select-none'>Checkbox 2</label>
	</div>

	<!-- 3 -->

	<div class='flex flex-row justify-center bg-gray-800 p-1'>
		<input type="checkbox" id="cb3" value="cb3"
        class='
            appearance-none h-6 w-2 bg-gray-400 
            checked:bg-yellow-300 checked:shadow-[0_0_5px_yellow]
            transition-all duration-300 peer
            ml-1
        '
    />
		<label for='cb3' class='flex flex-col justify-center px-2 peer-checked:text-yellow-300 select-none text-white'>Checkbox 3</label>
	</div>

	<!-- 4 -->

	<div class='flex flex-col justify-between bg-gray-800 '>
		<input type="checkbox" id="cb4" value="cb4"
        class='
            appearance-none h-1 w-full bg-gray-400 
            checked:bg-yellow-300 checked:shadow-[0_0px_5px_yellow]
            transition-all duration-300 peer
        '
    />
		<label for='cb4' class='p-1 flex flex-row justify-center px-2 peer-checked:text-yellow-300 select-none text-white'>Checkbox 4</label>
	</div>

	<!-- 5 -->

	<div class='flex flex-col justify-between bg-gray-800 relative
    '>
		<input type="checkbox" id="cb5" value="cb5"
        class='
            appearance-none peer
        '
    />
		<label for='cb5' class='p-1 flex flex-row justify-center px-2 select-none text-white peer-checked:text-green-300'>Checkbox 5</label>
		<div class='absolute w-full h-full peer-checked:shadow-[-4px_4px_0px_rgb(134,239,172)] 
        pointer-events-none transition-all duration-300'></div>
	</div>
</div>

<script>
	const childs = document.querySelectorAll('input');
    for(let i =0;i<childs.length;i++){
        window.setTimeout(function(){
            childs[i].checked = true; 
        },(i+1)*500);
    }
</script>'''
    },{
    "html":'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
    <div class="flex flex-col">
        <label for="input_show_hide_password">Show / Hide Password</label>
        <div x-data="{ show: false }" class="relative flex items-center mt-2">
            <input :type=" show ? 'text': 'password' " name="input_show_hide_password" id="input_show_hide_password" class="flex-1 p-2 pr-10 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300" value="password" type="password">
            <button type="button" class="absolute right-2 bg-transparent flex items-center justify-center hover:text-blue-600" @click="show = !show">
                <svg x-show="!show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>

                <svg x-show="show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="display: none;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
            </button>
        </div>
    </div>
</div>
</body>
</html>'''
    }
]
Alpinejs =[
    {
    "html":'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
    <div class="flex flex-col">
        <label for="input_show_hide_password">Show / Hide Password</label>
        <div x-data="{ show: false }" class="relative flex items-center mt-2">
            <input :type=" show ? 'text': 'password' " name="input_show_hide_password" id="input_show_hide_password" class="flex-1 p-2 pr-10 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300" value="password" type="password">
            <button type="button" class="absolute right-2 bg-transparent flex items-center justify-center hover:text-blue-600" @click="show = !show">
                <svg x-show="!show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>

                <svg x-show="show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="display: none;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
            </button>
        </div>
    </div>
</div>
</body>
</html>'''
    },{
    "html":'''<!-- This is an example component -->
<body x-data="imageGallery()" 
      x-init="fetch('https://pixabay.com/api/?key=15819227-ef2d84d1681b9442aaa9755b8&q=woman+girl+food&image_type=all&per_page=52&')
      .then(response => response.json())
      .then(response => { images = response.hits })"
      class="bg-white">

<div class="main">
    <div class="px-4 sm:px-8 lg:px-16 xl:px-20 mx-auto">

        <!-- hero -->
        <div class="hero">
            <!-- hero headline -->
            <div class="hero-headline flex flex-col items-center justify-center pt-24 text-center">
                <h1 class=" font-bold text-3xl text-gray-900">Stunning free images & royalty free stock</h1>
                <p class=" font-base text-base text-gray-600">high quality stock images and videos shared by our talented community.</p>
            </div>

            <!-- image search box -->
            <div class="box pt-6">
                <div class="box-wrapper">

                    <div class=" bg-white rounded flex items-center w-full p-3 shadow-sm border border-gray-200">
                      <button @click="getImages()" class="outline-none focus:outline-none"><svg class=" w-5 text-gray-600 h-5 cursor-pointer" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" stroke="currentColor" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg></button>
                      <input type="search" name="" id="" @keydown.enter="getImages()" placeholder="search for images" x-model="q" class="w-full pl-4 text-sm outline-none focus:outline-none bg-transparent">
                      <div class="select">
                        <select name="" id="" x-model="image_type" class="text-sm outline-none focus:outline-none bg-transparent">
                          <option value="all" selected>All</option>
                          <option value="photo">Photo</option>
                          <option value="illustration">Illustration</option>
                          <option value="vector">Vector</option>
                         </select>
                      </div>
                    </div>
                  
                </div>
            </div>

            <section id="photos" class="my-5 grid grid-cols-1 md:grid-cols-4 gap-4">
                <template x-for="image in images" :key="image.id">
                  <a :href="image.largeImageURL" class="hover:opacity-75 " target="_new"><img class="w-full h-64 object-cover" :src="image.largeImageURL" :alt="image.tags" /></a>
                </template>
              </section>

        </div>

        <footer class="p-5 text-sm text-gray-600 text-center inline-flex items-center">
          <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="heart" class="svg-inline--fa fa-heart fa-w-16 text-red-600 w-4 h-4 mr-4 align-middle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"></path></svg>
          <span>Made by <a href="https://tailwindcss.com/" target="_new" class="text-teal-600 font-semibold">tailwindcss</a> & <a href="https://github.com/alpinejs/alpine" target="_new" class="text-teal-600 font-semibold">alpinejs</a></span>
        </footer>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.3.5/dist/alpine.min.js" defer></script>
<script>
    function imageGallery() {
        return {
          images: [],
          api_key : "15819227-ef2d84d1681b9442aaa9755b8",
          q: "",
          image_type: "",
          page: "",
          per_page: 52,
          getImages: async function() {
            console.log("params", this.q, this.image_type);  
            const response = await fetch(
              `https://pixabay.com/api/?key=${this.api_key}&q=${
                this.q
              }&image_type=${this.image_type}&per_page=${this.per_page}&page=${this.page}`
            );
            const data = await response.json();
            this.images = data.hits;
          }
        };
      }
</script>'''
    },{
    "html":'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.5.1/chart.min.js"></script>
</head>
<body>
    <div class="h-full bg-gray-200 p-8">
        <div class="bg-white rounded-lg shadow-xl pb-8">
            <div x-data="{ openSettings: false }" class="absolute right-12 mt-4 rounded">
                <button @click="openSettings = !openSettings" class="border border-gray-400 p-2 rounded text-gray-300 hover:text-gray-300 bg-gray-100 bg-opacity-10 hover:bg-opacity-20" title="Settings">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"></path>
                    </svg>
                </button>
                <div x-show="openSettings" @click.away="openSettings = false" class="bg-white absolute right-0 w-40 py-2 mt-1 border border-gray-200 shadow-2xl" style="display: none;">
                    <div class="py-2 border-b">
                        <p class="text-gray-400 text-xs px-6 uppercase mb-1">Settings</p>
                        <button class="w-full flex items-center px-6 py-1.5 space-x-2 hover:bg-gray-200">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path>
                            </svg>
                            <span class="text-sm text-gray-700">Share Profile</span>
                        </button>
                        <button class="w-full flex items-center py-1.5 px-6 space-x-2 hover:bg-gray-200">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636"></path>
                            </svg>
                            <span class="text-sm text-gray-700">Block User</span>
                        </button>
                        <button class="w-full flex items-center py-1.5 px-6 space-x-2 hover:bg-gray-200">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                            <span class="text-sm text-gray-700">More Info</span>
                        </button>
                    </div>
                    <div class="py-2">
                        <p class="text-gray-400 text-xs px-6 uppercase mb-1">Feedback</p>
                        <button class="w-full flex items-center py-1.5 px-6 space-x-2 hover:bg-gray-200">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                            </svg>
                            <span class="text-sm text-gray-700">Report</span>
                        </button>
                    </div>
                </div>
            </div>
            <div class="w-full h-[250px]">
                <img src="https://vojislavd.com/ta-template-demo/assets/img/profile-background.jpg" class="w-full h-full rounded-tl-lg rounded-tr-lg">
            </div>
            <div class="flex flex-col items-center -mt-20">
                <img src="https://vojislavd.com/ta-template-demo/assets/img/profile.jpg" class="w-40 border-4 border-white rounded-full">
                <div class="flex items-center space-x-2 mt-2">
                    <p class="text-2xl">Amanda Ross</p>
                    <span class="bg-blue-500 rounded-full p-1" title="Verified">
                        <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-100 h-2.5 w-2.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M5 13l4 4L19 7"></path>
                        </svg>
                    </span>
                </div>
                <p class="text-gray-700">Senior Software Engineer at Tailwind CSS</p>
                <p class="text-sm text-gray-500">New York, USA</p>
            </div>
            <div class="flex-1 flex flex-col items-center lg:items-end justify-end px-8 mt-2">
                <div class="flex items-center space-x-4 mt-2">
                    <button class="flex items-center bg-blue-600 hover:bg-blue-700 text-gray-100 px-4 py-2 rounded text-sm space-x-2 transition duration-100">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z"></path>
                        </svg>
                        <span>Connect</span>
                    </button>
                    <button class="flex items-center bg-blue-600 hover:bg-blue-700 text-gray-100 px-4 py-2 rounded text-sm space-x-2 transition duration-100">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z" clip-rule="evenodd"></path>
                        </svg>
                        <span>Message</span>
                    </button>
                </div>
            </div>
        </div>

        <div class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4">
            <div class="w-full flex flex-col 2xl:w-1/3">
                <div class="flex-1 bg-white rounded-lg shadow-xl p-8">
                    <h4 class="text-xl text-gray-900 font-bold">Personal Info</h4>
                    <ul class="mt-2 text-gray-700">
                        <li class="flex border-y py-2">
                            <span class="font-bold w-24">Full name:</span>
                            <span class="text-gray-700">Amanda S. Ross</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-24">Birthday:</span>
                            <span class="text-gray-700">24 Jul, 1991</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-24">Joined:</span>
                            <span class="text-gray-700">10 Jan 2022 (25 days ago)</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-24">Mobile:</span>
                            <span class="text-gray-700">(123) 123-1234</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-24">Email:</span>
                            <span class="text-gray-700">amandaross@example.com</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-24">Location:</span>
                            <span class="text-gray-700">New York, US</span>
                        </li>
                        <li class="flex border-b py-2">
                            <span class="font-bold w-24">Languages:</span>
                            <span class="text-gray-700">English, Spanish</span>
                        </li>
                        <li class="flex items-center border-b py-2 space-x-2">
                            <span class="font-bold w-24">Elsewhere:</span>
                            <a href="#" title="Facebook">
                                <svg class="w-5 h-5" id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 506.86 506.86"><defs><style>.cls-1{fill:#1877f2;}.cls-2{fill:#fff;}</style></defs><path class="cls-1" d="M506.86,253.43C506.86,113.46,393.39,0,253.43,0S0,113.46,0,253.43C0,379.92,92.68,484.77,213.83,503.78V326.69H149.48V253.43h64.35V197.6c0-63.52,37.84-98.6,95.72-98.6,27.73,0,56.73,5,56.73,5v62.36H334.33c-31.49,0-41.3,19.54-41.3,39.58v47.54h70.28l-11.23,73.26H293V503.78C414.18,484.77,506.86,379.92,506.86,253.43Z"></path><path class="cls-2" d="M352.08,326.69l11.23-73.26H293V205.89c0-20,9.81-39.58,41.3-39.58h31.95V104s-29-5-56.73-5c-57.88,0-95.72,35.08-95.72,98.6v55.83H149.48v73.26h64.35V503.78a256.11,256.11,0,0,0,79.2,0V326.69Z"></path></svg>
                            </a>
                            <a href="#" title="Twitter">
                                <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 333333 333333" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd"><path d="M166667 0c92048 0 166667 74619 166667 166667s-74619 166667-166667 166667S0 258715 0 166667 74619 0 166667 0zm90493 110539c-6654 2976-13822 4953-21307 5835 7669-4593 13533-11870 16333-20535-7168 4239-15133 7348-23574 9011-6787-7211-16426-11694-27105-11694-20504 0-37104 16610-37104 37101 0 2893 320 5722 949 8450-30852-1564-58204-16333-76513-38806-3285 5666-5022 12109-5022 18661v4c0 12866 6532 24246 16500 30882-6083-180-11804-1876-16828-4626v464c0 17993 12789 33007 29783 36400-3113 845-6400 1313-9786 1313-2398 0-4709-247-7007-665 4746 14736 18448 25478 34673 25791-12722 9967-28700 15902-46120 15902-3006 0-5935-184-8860-534 16466 10565 35972 16684 56928 16684 68271 0 105636-56577 105636-105632 0-1630-36-3209-104-4806 7251-5187 13538-11733 18514-19185l17-17-3 2z" fill="#1da1f2"></path></svg>
                            </a>
                            <a href="#" title="LinkedIn">
                                <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 333333 333333" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd"><path d="M166667 0c92048 0 166667 74619 166667 166667s-74619 166667-166667 166667S0 258715 0 166667 74619 0 166667 0zm-18220 138885h28897v14814l418 1c4024-7220 13865-14814 28538-14814 30514-1 36157 18989 36157 43691v50320l-30136 1v-44607c0-10634-221-24322-15670-24322-15691 0-18096 11575-18096 23548v45382h-30109v-94013zm-20892-26114c0 8650-7020 15670-15670 15670s-15672-7020-15672-15670 7022-15670 15672-15670 15670 7020 15670 15670zm-31342 26114h31342v94013H96213v-94013z" fill="#0077b5"></path></svg>
                            </a>
                            <a href="#" title="Github">
                                <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" width="0" height="0" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd" viewBox="0 0 640 640"><path d="M319.988 7.973C143.293 7.973 0 151.242 0 327.96c0 141.392 91.678 261.298 218.826 303.63 16.004 2.964 21.886-6.957 21.886-15.414 0-7.63-.319-32.835-.449-59.552-89.032 19.359-107.8-37.772-107.8-37.772-14.552-36.993-35.529-46.831-35.529-46.831-29.032-19.879 2.209-19.442 2.209-19.442 32.126 2.245 49.04 32.954 49.04 32.954 28.56 48.922 74.883 34.76 93.131 26.598 2.882-20.681 11.15-34.807 20.315-42.803-71.08-8.067-145.797-35.516-145.797-158.14 0-34.926 12.52-63.485 32.965-85.88-3.33-8.078-14.291-40.606 3.083-84.674 0 0 26.87-8.61 88.029 32.8 25.512-7.075 52.878-10.642 80.056-10.76 27.2.118 54.614 3.673 80.162 10.76 61.076-41.386 87.922-32.8 87.922-32.8 17.398 44.08 6.485 76.631 3.154 84.675 20.516 22.394 32.93 50.953 32.93 85.879 0 122.907-74.883 149.93-146.117 157.856 11.481 9.921 21.733 29.398 21.733 59.233 0 42.792-.366 77.28-.366 87.804 0 8.516 5.764 18.473 21.992 15.354 127.076-42.354 218.637-162.274 218.637-303.582 0-176.695-143.269-319.988-320-319.988l-.023.107z"></path></svg>
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="flex-1 bg-white rounded-lg shadow-xl mt-4 p-8">
                    <h4 class="text-xl text-gray-900 font-bold">Activity log</h4>
                    <div class="relative px-4">
                        <div class="absolute h-full border border-dashed border-opacity-20 border-secondary"></div>

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">Profile informations changed.</p>
                                <p class="text-xs text-gray-500">3 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Connected with <a href="#" class="text-blue-600 font-bold">Colby Covington</a>.</p>
                                <p class="text-xs text-gray-500">15 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">Invoice <a href="#" class="text-blue-600 font-bold">#4563</a> was created.</p>
                                <p class="text-xs text-gray-500">57 min ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Message received from <a href="#" class="text-blue-600 font-bold">Cecilia Hendric</a>.</p>
                                <p class="text-xs text-gray-500">1 hour ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">New order received <a href="#" class="text-blue-600 font-bold">#OR9653</a>.</p>
                                <p class="text-xs text-gray-500">2 hours ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->

                        <!-- start::Timeline item -->
                        <div class="flex items-center w-full my-6 -ml-1.5">
                            <div class="w-1/12 z-10">
                                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
                            </div>
                            <div class="w-11/12">
                                <p class="text-sm">
                                    Message received from <a href="#" class="text-blue-600 font-bold">Jane Stillman</a>.</p>
                                <p class="text-xs text-gray-500">2 hours ago</p>
                            </div>
                        </div>
                        <!-- end::Timeline item -->
                    </div>
                </div>
            </div>
            <div class="flex flex-col w-full 2xl:w-2/3">
                <div class="flex-1 bg-white rounded-lg shadow-xl p-8">
                    <h4 class="text-xl text-gray-900 font-bold">About</h4>
                    <p class="mt-2 text-gray-700">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt voluptates obcaecati numquam error et ut fugiat asperiores. Sunt nulla ad incidunt laboriosam, laudantium est unde natus cum numquam, neque facere. Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut, magni odio magnam commodi sunt ipsum eum! Voluptas eveniet aperiam at maxime, iste id dicta autem odio laudantium eligendi commodi distinctio!</p>
                </div>
                <div class="flex-1 bg-white rounded-lg shadow-xl mt-4 p-8">
                    <h4 class="text-xl text-gray-900 font-bold">Statistics</h4>
                    
                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mt-4">
                        <div class="px-6 py-6 bg-gray-100 border border-gray-300 rounded-lg shadow-xl">
                            <div class="flex items-center justify-between">
                                <span class="font-bold text-sm text-indigo-600">Total Revenue</span>
                                <span class="text-xs bg-gray-200 hover:bg-gray-500 text-gray-500 hover:text-gray-200 px-2 py-1 rounded-lg transition duration-200 cursor-default">7 days</span>
                            </div>
                            <div class="flex items-center justify-between mt-6">
                                <div>
                                    <svg class="w-12 h-12 p-2.5 bg-indigo-400 bg-opacity-20 rounded-full text-indigo-600 border border-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                </div>
                                <div class="flex flex-col">
                                    <div class="flex items-end">
                                        <span class="text-2xl 2xl:text-3xl font-bold">$8,141</span>
                                        <div class="flex items-center ml-2 mb-1">
                                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                                            <span class="font-bold text-sm text-gray-500 ml-0.5">3%</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="px-6 py-6 bg-gray-100 border border-gray-300 rounded-lg shadow-xl">
                            <div class="flex items-center justify-between">
                                <span class="font-bold text-sm text-green-600">New Orders</span>
                                <span class="text-xs bg-gray-200 hover:bg-gray-500 text-gray-500 hover:text-gray-200 px-2 py-1 rounded-lg transition duration-200 cursor-default">7 days</span>
                            </div>
                            <div class="flex items-center justify-between mt-6">
                                <div>
                                    <svg class="w-12 h-12 p-2.5 bg-green-400 bg-opacity-20 rounded-full text-green-600 border border-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
                                </div>
                                <div class="flex flex-col">
                                    <div class="flex items-end">
                                        <span class="text-2xl 2xl:text-3xl font-bold">217</span>
                                        <div class="flex items-center ml-2 mb-1">
                                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                                            <span class="font-bold text-sm text-gray-500 ml-0.5">5%</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="px-6 py-6 bg-gray-100 border border-gray-300 rounded-lg shadow-xl">
                            <div class="flex items-center justify-between">
                                <span class="font-bold text-sm text-blue-600">New Connections</span>
                                <span class="text-xs bg-gray-200 hover:bg-gray-500 text-gray-500 hover:text-gray-200 px-2 py-1 rounded-lg transition duration-200 cursor-default">7 days</span>
                            </div>
                            <div class="flex items-center justify-between mt-6">
                                <div>
                                    <svg class="w-12 h-12 p-2.5 bg-blue-400 bg-opacity-20 rounded-full text-blue-600 border border-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                </div>
                                <div class="flex flex-col">
                                    <div class="flex items-end">
                                        <span class="text-2xl 2xl:text-3xl font-bold">54</span>
                                        <div class="flex items-center ml-2 mb-1">
                                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                                            <span class="font-bold text-sm text-gray-500 ml-0.5">7%</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="mt-4">
                        <canvas id="verticalBarChart" style="display: block; box-sizing: border-box; height: 414px; width: 828px;" width="1656" height="828"></canvas>
                    </div>
                </div>
            </div>
        </div>
        <div class="bg-white rounded-lg shadow-xl p-8">
            <div class="flex items-center justify-between">
                <h4 class="text-xl text-gray-900 font-bold">Connections (532)</h4>
                <a href="#" title="View All">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-500 hover:text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path>
                    </svg>
                </a>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-8 gap-8 mt-8">
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection1.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Diane Aguilar</p>
                    <p class="text-xs text-gray-500 text-center">UI/UX Design at Upwork</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection2.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Frances Mather</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer at Facebook</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection3.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Carlos Friedrich</p>
                    <p class="text-xs text-gray-500 text-center">Front-End Developer at Tailwind CSS</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection4.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Donna Serrano</p>
                    <p class="text-xs text-gray-500 text-center">System Engineer at Tesla</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection5.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Randall Tabron</p>
                    <p class="text-xs text-gray-500 text-center">Software Developer at Upwork</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection6.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">John McCleary</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer at Laravel</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection7.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Amanda Noble</p>
                    <p class="text-xs text-gray-500 text-center">Graphic Designer at Tailwind CSS</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection8.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Christine Drew</p>
                    <p class="text-xs text-gray-500 text-center">Senior Android Developer at Google</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection9.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Lucas Bell</p>
                    <p class="text-xs text-gray-500 text-center">Creative Writer at Upwork</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection10.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Debra Herring</p>
                    <p class="text-xs text-gray-500 text-center">Co-Founder at Alpine.js</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection11.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Benjamin Farrior</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer Lead at Microsoft</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection12.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Maria Heal</p>
                    <p class="text-xs text-gray-500 text-center">Linux System Administrator at Twitter</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection13.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Edward Ice</p>
                    <p class="text-xs text-gray-500 text-center">Customer Support at Instagram</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection14.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Jeffery Silver</p>
                    <p class="text-xs text-gray-500 text-center">Software Engineer at Twitter</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection15.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Jennifer Schultz</p>
                    <p class="text-xs text-gray-500 text-center">Project Manager at Google</p>
                </a>
                <a href="#" class="flex flex-col items-center justify-center text-gray-800 hover:text-blue-600" title="View Profile">
                    <img src="https://vojislavd.com/ta-template-demo/assets/img/connections/connection16.jpg" class="w-16 rounded-full">
                    <p class="text-center font-bold text-sm mt-1">Joseph Marlatt</p>
                    <p class="text-xs text-gray-500 text-center">Team Lead at Facebook</p>
                </a>
            </div>
        </div>
    </div>

    <script>

            const DATA_SET_VERTICAL_BAR_CHART_1 = [68.106, 26.762, 94.255, 72.021, 74.082, 64.923, 85.565, 32.432, 54.664, 87.654, 43.013, 91.443];

            const labels_vertical_bar_chart = ['January', 'February', 'Mart', 'April', 'May', 'Jun', 'July', 'August', 'September', 'October', 'November', 'December'];

            const dataVerticalBarChart= {
                labels: labels_vertical_bar_chart,
                datasets: [
                    {
                        label: 'Revenue',
                        data: DATA_SET_VERTICAL_BAR_CHART_1,
                        borderColor: 'rgb(54, 162, 235)',
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    }
                ]
            };
            const configVerticalBarChart = {
                type: 'bar',
                data: dataVerticalBarChart,
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        title: {
                            display: true,
                            text: 'Last 12 Months'
                        }
                    }
                },
            };

            var verticalBarChart = new Chart(
                document.getElementById('verticalBarChart'),
                configVerticalBarChart
            );
        </script>
</body>
</html>'''
    },{
    "html":'''<link rel="stylesheet" href="https://unpkg.com/boxicons@2.1.2/css/boxicons.min.css" />
<script defer src="https://unpkg.com/alpinejs@3.7.0/dist/cdn.min.js"></script>

<!-- page -->
<main x-data="app" class="min-w-screen flex min-h-screen items-center justify-center">
  <!-- toast -->
  <button type="button" @click="closeToast()" x-show="open" x-transition.duration.300ms class="fixed top-4 right-4 z-50 rounded-md bg-green-500 px-4 py-2 text-white transition hover:bg-green-600">
    <div class="flex items-center space-x-2">
      <span class="text-3xl"><i class="bx bx-check"></i></span>
      <p class="font-bold">Item Created Successfully!</p>
    </div>
  </button>

  <!-- trigger button -->
  <button type="button" @click="openToast()" class="rounded-md bg-blue-500 px-4 py-2 font-bold text-white transition hover:bg-blue-600">Launch toast</button>
</main>

<script>
  let timer;

  document.addEventListener("alpine:init", () => {
      Alpine.data("app", () => ({
          open: false,

          openToast() {
              if (this.open) return;
              this.open = true;

              // reset time to 0 second
              clearTimeout(timer);

              // auto close toast after 5 seconds
              timer = setTimeout(() => {
                  this.open = false;
              }, 5000);
          },

          closeToast() {
              this.open = false;
          },
      }));
  });
</script>'''
    },{
    "html":'''<!-- component -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
    <div x-data="{ 
        billingType: 'month', 
        basicPrice: '19',
        premiumPrice: '29',
        proPrice: '39'
    }" class="min-h-full bg-gray-200 pb-12">
    <div class="w-full bg-blue-900 pt-16 pb-24 text-center">
        <h4 class="text-2xl text-gray-100">Choose the right plan for you</h4>
        <p class="text-sm text-gray-100 mt-2">Pricing built for businesses of all sizes. Choose package that suits your needs.</p>
        <div class="flex items-center justify-center mt-8">
            <button @click="
                    billingType = 'month',
                    basicPrice = '19',
                    premiumPrice = '29',
                    proPrice = '39'
                " class="text-gray-800 px-4 py-2 rounded-tl-lg rounded-bl-lg bg-gray-200" :class=" billingType === 'month' ? 'bg-blue-300' : 'bg-gray-200' " title="Choose Monthly billing">
                Monthly billing
            </button>
            <button @click="
                    billingType = 'year',
                    basicPrice = '205',
                    premiumPrice = '313',
                    proPrice = '421'
                " class="text-gray-800 px-4 py-2 rounded-tr-lg rounded-br-lg bg-gray-200" :class=" billingType === 'year' ? 'bg-blue-300' : 'bg-gray-200' " title="Choose Annual billing">
                Annual billing
            </button>
        </div>
    </div>
    <div class="w-full 2xl:w-3/4 flex items-center justify-center px-8 md:px-32 lg:px-16 2xl:px-0 mx-auto -mt-8">
        <div class="w-full grid grid-cols-1 xl:grid-cols-3 gap-8">
            <div class="bg-white shadow-2xl rounded-lg py-4">
                <p class="text-xl text-center font-bold text-blue-600">Basic</p>
                <p class="text-center py-8">
                    <span class="text-4xl font-bold text-gray-700">
                        $<span x-text="basicPrice">19</span>    
                    </span>
                    <span class="text-xs uppercase text-gray-500">
                        / <span x-text="billingType">month</span>
                    </span>
                </p>
                <ul class="border-t border-gray-300 py-8 space-y-6">
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Free Setup Guidance</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Email Support</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">User Management</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Reports</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-gray-300 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-400 capitalize">Unlimited Users</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-gray-300 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-400 capitalize">Data Export</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-gray-300 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-400 capitalize">Automated Workflows</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-gray-300 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-400 capitalize">API Access</span>
                    </li>
                </ul>
                <div class="flex items-center justify-center mt-6">
                    <a href="#" class="bg-blue-600 hover:bg-blue-700 px-8 py-2 text-sm text-gray-200 uppercase rounded font-bold transition duration-150" title="Purchase">Purchase</a>
                </div>
            </div>
            <div class="bg-white shadow-2xl rounded-lg py-4">
                <p class="text-xl text-center font-bold text-blue-600">Premium</p>
                <p class="text-center py-8">
                    <span class="text-4xl font-bold text-gray-700">
                        $<span x-text="premiumPrice">29</span>
                    </span>
                    <span class="text-xs uppercase text-gray-500">
                        / <span x-text="billingType">month</span>
                    </span>
                </p>
                <ul class="border-t border-gray-300 py-8 space-y-6">
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Free Setup Guidance</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Email Support</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">User Management</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Reports</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Unlimited Users</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Data Export</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-gray-300 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-400 capitalize">Automated Workflows</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-gray-300 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-400 capitalize">API Access</span>
                    </li>
                </ul>
                <div class="flex items-center justify-center mt-6">
                    <a href="#" class="bg-blue-600 hover:bg-blue-700 px-8 py-2 text-sm text-gray-200 uppercase rounded font-bold transition duration-150" title="Purchase">Purchase</a>
                </div>
            </div>
            <div class="bg-white shadow-2xl rounded-lg py-4">
                <p class="text-xl text-center font-bold text-blue-600">Pro</p>
                <p class="text-center py-8">
                    <span class="text-4xl font-bold text-gray-700">
                        $<span x-text="proPrice">39</span>
                    </span>
                    <span class="text-xs uppercase text-gray-500">
                        / <span x-text="billingType">month</span>
                    </span>
                </p>
                <ul class="border-t border-gray-300 py-8 space-y-6">
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Free Setup Guidance</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Email Support</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">User Management</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Reports</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Unlimited Users</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Data Export</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">Automated Workflows</span>
                    </li>
                    <li class="flex items-center space-x-2 px-8">
                        <span class="bg-blue-600 rounded-full p-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <span class="text-gray-600 capitalize">API Access</span>
                    </li>
                </ul>
                <div class="flex items-center justify-center mt-6">
                    <a href="#" class="bg-blue-600 hover:bg-blue-700 px-8 py-2 text-sm text-gray-200 uppercase rounded font-bold transition duration-150" title="Purchase">Purchase</a>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>'''
    },{
    "html":'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
    <div class="w-full h-screen" style="background-image: url('https://vojislavd.com/ta-template-demo/assets/img/coming-soon.jpg');">
        <div class="w-full h-screen bg-black bg-opacity-70">
            <div class="w-full h-full flex flex-col items-start justify-between container mx-auto py-8 px-8 lg:px-4 xl:px-0">
                <div class="bg-white bg-opacity-10 px-4 py-2 rounded-xl flex items-center justify-center text-cyan-100 space-x-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 lg:h-8 w-6 lg:w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path>
                    </svg>
                    <span class="text-lg lg:text-2xl font-bold">Template</span>
                </div>
                <div class="flex-1 flex flex-col items-start justify-center">
                    <h1 class="text-6xl lg:text-7xl xl:text-8xl text-gray-200 tracking-wider font-bold font-serif mt-12 text-center md:text-left">We Are <span class="text-yellow-300">Coming</span> Soon</h1>
                    
                    <div class="mt-12 flex flex-col items-center mt-8 ml-2">
                        <p class="text-gray-300 uppercase text-sm">Time left until lunching</p>
                        <div class="flex items-center justify-center space-x-4 mt-4" x-data="timer(new Date().setDate(new Date().getDate() + 1))" x-init="init();">
                            <div class="flex flex-col items-center px-4">
                                <span x-text="time().days" class="text-4xl lg:text-5xl text-gray-200">00</span>
                                <span class="text-gray-400 mt-2">Days</span>
                            </div>
                            <span class="w-[1px] h-24 bg-gray-400"></span>
                            <div class="flex flex-col items-center px-4">
                                <span x-text="time().hours" class="text-4xl lg:text-5xl text-gray-200">23</span>
                                <span class="text-gray-400 mt-2">Hours</span>
                            </div>
                            <span class="w-[1px] h-24 bg-gray-400"></span>
                            <div class="flex flex-col items-center px-4">
                                <span x-text="time().minutes" class="text-4xl lg:text-5xl text-gray-200">59</span>
                                <span class="text-gray-400 mt-2">Minutes</span>
                            </div>
                            <span class="w-[1px] h-24 bg-gray-400"></span>
                            <div class="flex flex-col items-center px-4">
                                <span x-text="time().seconds" class="text-4xl lg:text-5xl text-gray-200">28</span>
                                <span class="text-gray-400 mt-2">Seconds</span>
                            </div>
                        </div>                      
                    </div>
                    <div class="flex flex-col items-center space-y-4 mt-16 px-6">
                        <p class="text-gray-300 uppercase text-sm">Notify me when it's ready</p>
                        <form class="w-full flex items-center">
                            <input type="email" name="email" id="email" class="w-72 p-2 border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded-tl rounded-bl text-sm" placeholder="Email" autocomplete="off">
                            <button class="bg-blue-600 py-2 px-6 text-gray-100 border border-blue-600 rounded-tr rounded-br text-sm">Subscribe</button>
                        </form>
                    </div>
                </div>
                <div class="w-full flex items-center justify-center md:justify-end">
                    <ul class="flex items-center space-x-4">
                        <li>
                            <a href="#" title="Facebook">
                                <svg class="w-8 h-8 hover:scale-110 transition duration-300" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 506.86 506.86"><defs><style>.cls-1{fill:#e2e8f0;}</style></defs><path class="cls-1" d="M506.86,253.43C506.86,113.46,393.39,0,253.43,0S0,113.46,0,253.43C0,379.92,92.68,484.77,213.83,503.78V326.69H149.48V253.43h64.35V197.6c0-63.52,37.84-98.6,95.72-98.6,27.73,0,56.73,5,56.73,5v62.36H334.33c-31.49,0-41.3,19.54-41.3,39.58v47.54h70.28l-11.23,73.26H293V503.78C414.18,484.77,506.86,379.92,506.86,253.43Z"></path><path class="cls-2" d="M352.08,326.69l11.23-73.26H293V205.89c0-20,9.81-39.58,41.3-39.58h31.95V104s-29-5-56.73-5c-57.88,0-95.72,35.08-95.72,98.6v55.83H149.48v73.26h64.35V503.78a256.11,256.11,0,0,0,79.2,0V326.69Z"></path></svg>
                            </a>
                        </li>
                        <li>
                            <a href="#" title="Twitter">
                                <svg class="w-8 h-8 hover:scale-110 transition duration-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 333333 333333" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd"><path d="M166667 0c92048 0 166667 74619 166667 166667s-74619 166667-166667 166667S0 258715 0 166667 74619 0 166667 0zm90493 110539c-6654 2976-13822 4953-21307 5835 7669-4593 13533-11870 16333-20535-7168 4239-15133 7348-23574 9011-6787-7211-16426-11694-27105-11694-20504 0-37104 16610-37104 37101 0 2893 320 5722 949 8450-30852-1564-58204-16333-76513-38806-3285 5666-5022 12109-5022 18661v4c0 12866 6532 24246 16500 30882-6083-180-11804-1876-16828-4626v464c0 17993 12789 33007 29783 36400-3113 845-6400 1313-9786 1313-2398 0-4709-247-7007-665 4746 14736 18448 25478 34673 25791-12722 9967-28700 15902-46120 15902-3006 0-5935-184-8860-534 16466 10565 35972 16684 56928 16684 68271 0 105636-56577 105636-105632 0-1630-36-3209-104-4806 7251-5187 13538-11733 18514-19185l17-17-3 2z" fill="#e2e8f0"></path></svg>
                            </a>
                        </li>
                        <li>
                            <a href="#" title="LinkedIn">
                                <svg class="w-8 h-8 hover:scale-110 transition duration-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 333333 333333" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd"><path d="M166667 0c92048 0 166667 74619 166667 166667s-74619 166667-166667 166667S0 258715 0 166667 74619 0 166667 0zm-18220 138885h28897v14814l418 1c4024-7220 13865-14814 28538-14814 30514-1 36157 18989 36157 43691v50320l-30136 1v-44607c0-10634-221-24322-15670-24322-15691 0-18096 11575-18096 23548v45382h-30109v-94013zm-20892-26114c0 8650-7020 15670-15670 15670s-15672-7020-15672-15670 7022-15670 15672-15670 15670 7020 15670 15670zm-31342 26114h31342v94013H96213v-94013z" fill="#e2e8f0"></path></svg>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        function timer(expiry) {
            return {
                expiry: expiry,
                remaining:null,
                init() {
                this.setRemaining()
                setInterval(() => {
                    this.setRemaining();
                }, 1000);
                },
                setRemaining() {
                const diff = this.expiry - new Date().getTime();
                this.remaining =  parseInt(diff / 1000);
                },
                days() {
                return {
                    value:this.remaining / 86400,
                    remaining:this.remaining % 86400
                };
                },
                hours() {
                return {
                    value:this.days().remaining / 3600,
                    remaining:this.days().remaining % 3600
                };
                },
                minutes() {
                    return {
                    value:this.hours().remaining / 60,
                    remaining:this.hours().remaining % 60
                };
                },
                seconds() {
                    return {
                    value:this.minutes().remaining,
                };
                },
                format(value) {
                return ("0" + parseInt(value)).slice(-2)
                },
                time(){
                    return {
                    days:this.format(this.days().value),
                    hours:this.format(this.hours().value),
                    minutes:this.format(this.minutes().value),
                    seconds:this.format(this.seconds().value),
                }
                },
            }
        }
    </script>
</body>
</html>'''
    },{
    "html":'''<!-- This is an example component -->
<script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
<div x-data="{show: false, product:['apple','orange','avocado','mango','peer'],
email: '',
password: '',
toggle: '0',
}" class="max-w-md px-3 rounded-lg mx-auto overflow-hidden mt-4 bg-white">
   	<div class="flex flex-col mt-8 mb-5">
   		<div class="relative">
   			<input type="text" x-model="email" name="email" class="w-full px-4 mb-3 rounded border py-2">
   			<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="absolute bottom-5 right-5 inline w-6 h-6">
			  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
			</svg>

   			</div>
   			<div class="flex mb-1 justify-between">
   				<div class="mb-3 relative rounded-full w-12 h-6 transition duration-200 ease-linear"
         :class="[toggle === '1' ? 'bg-green-400' : 'bg-red-400']">
		    <label for="toggle"
		           class="absolute left-0 bg-white border-2 mb-2 w-6 h-6 rounded-full transition transform duration-100 ease-linear cursor-pointer"
		           :class="[toggle === '1' ? 'translate-x-full border-green-400' : 'translate-x-0 border-red-400']"></label>
		    <input type="checkbox" id="toggle" name="toggle"
		           class="appearance-none w-full h-full active:outline-none focus:outline-none"
		           @click="toggle === '0' ? toggle = '1' : toggle = '0'"/>
		  </div>
   				<a href="" class="text-sm text-rigth font-semibold text-blue-500">forgot password?</a>
   			</div>
   			<div class="relative items-center"> 
   			<input :type="show ? 'text' : 'password' " x-model="password" name="password" class="w-full px-4 mb-5 rounded border py-2">
   			<button @click="show = !show" class="absolute inline-block bottom-7 right-5">
	   		<svg x-show="!show" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
	             <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />
	        </svg>
	        <svg x-show="show" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
			  <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
			  <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
			</svg>

	        </button>
	       </div>
           <button type="submit" class="py-1 mb-3 px-3 rounded text-white bg-blue-500 shadow-lg shadow-blue-500/50">Login</button>
   		
   	</div>
   </div>'''
    },{
    "html":'''<!-- This is an example component -->
<div>
    <!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.11/tailwind.min.css'>
   <script src='https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.3.2/cdn.js'></script>
</head>
<body>

<div class="antialiased min-h-screen bg-gray-100 flex items-center">
  
<div class="w-full max-w-sm mx-auto">
  <div class="bg-white shadow rounded-lg p-5 dark:bg-gray-800 w-full"
	x-data="{
		weatherData: null,
		fetchWeatherData() {
			fetch('https://api.weatherapi.com/v1/forecast.json?key=ff9b41622f994b1287a73535210809&q=Guwahati&days=3')
				.then(response => response.json())
				.then(json => this.weatherData = json)
		},
		formattedDateDisplay(date) {
			const options = {
				weekday: 'long',
				year: 'numeric',
				month: 'long',
				day: 'numeric'
		   };
		   
		   return (new Date(date)).toLocaleDateString('en-US', options);
		}
	}"
	x-init="fetchWeatherData()"
	x-cloak
>
	<h2 class="font-bold text-gray-800 text-lg dark:text-gray-400" x-text="formattedDateDisplay(new Date())"></h2>
	
	<template x-if="weatherData != null">
		<div>
			<div class="flex mt-4 mb-2">
				<div class="flex-1">
					<div class="text-gray-600 text-sm dark:text-gray-400" x-text="weatherData.location.name +', '+ weatherData.location.region"></div>
					<div class="text-3xl font-bold text-gray-800 dark:text-gray-300" x-html="`${weatherData.current.temp_c} &deg;C`"></div>
					<div x-text="weatherData.current.condition.text" class="text-xs text-gray-600 dark:text-gray-400"></div>
				</div>
				<div class="w-24">
					<img :src="`https:${weatherData.current.condition.icon}`" :alt="weatherData.current.condition.text" loading="lazy">
				</div>
			</div>

			<div class="flex space-x-2 justify-between border-t dark:border-gray-500">
				<template x-for="(forecast, key) in weatherData.forecast.forecastday.splice(1)">
					<div class="flex-1 text-center pt-3" :class="{'border-r dark:border-gray-500': key==0}">
						<div x-text="`${forecast.date.split('-')[2]}/${forecast.date.split('-')[1]}/${forecast.date.split('-')[0]}`" class="text-xs text-gray-500 dark:text-gray-400"></div>
						<img :src="`https:${forecast.day.condition.icon}`" :alt="forecast.day.condition.text" loading="lazy" class="mx-auto">
						<div x-html="`${forecast.day.maxtemp_c} &deg;C`" class="font-semibold text-gray-800 mt-1.5 dark:text-gray-300"></div>
						<div x-text="forecast.day.condition.text" class="text-xs text-gray-600 dark:text-gray-400"></div>
					</div>
				</template>
			</div>
		</div>
	</template>

	<template x-if="weatherData == null">
		<div class="animate-pulse">
			<div class="flex mt-4 mb-5">
				<div class="flex-1">
					<div class="rounded h-2 mb-1.5 bg-gray-200 w-1/2"></div>
					<div class="bg-gray-200 rounded h-4"></div>
					<div class="rounded h-2 mt-1.5 bg-gray-200 w-1/2"></div>
				</div>
				<div class="w-24">
					<div class="w-12 h-12 rounded-full bg-gray-100 mx-auto"></div>
				</div>
			</div>

			<div class="flex space-x-2 justify-between border-t h-32 dark:border-gray-500">
				<div class="flex-1 text-center pt-4 border-r px-5 dark:border-gray-500">
					<div class="rounded h-2 mb-2 bg-gray-200 w-1/2 mx-auto"></div>
					<div class="w-12 h-12 rounded-full bg-gray-100 mx-auto mb-2"></div>
					<div class="rounded h-3 mt-1 bg-gray-200 mt-1.5 mx-auto"></div>
					<div class="rounded h-2 mt-1 bg-gray-200 w-1/2 mx-auto"></div>
					
				</div>
				<div class="flex-1 text-center pt-4 px-5">
					<div class="rounded h-2 mb-2 bg-gray-200 w-1/2 mx-auto"></div>
					<div class="w-12 h-12 rounded-full bg-gray-100 mx-auto mb-2"></div>
					<div class="rounded h-3 mt-1 bg-gray-200 mt-1.5 mx-auto"></div>
					<div class="rounded h-2 mt-1 bg-gray-200 w-1/2 mx-auto"></div>
				</div>
			</div>
		</div>
	</template>
</div>
  
  <div class="mt-10">
                Build with <a class="underline text-purple-600" href="weatherapi.com">Weatherapi.com</a>, <a class="underline text-purple-600" href="https://tailwindcss.com/">TailwindCSS</a> & <a class="underline text-purple-600" href="https://alpinejs.dev/">Alpine.js</a>.
                <br>
                Github Gist: <a class="underline text-purple-600" href="https://gist.github.com/mithicher/70647625163c3d217c742dfc4a0b84c0">Weather Forecast Blade Component</a>
            </div>
</div>
  </div
</body>
</html>
</div>'''
    },{
    "html":'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
    <div class="bg-gray-200 w-full min-h-screen flex items-center justify-center">
            <div class="lg:flex items-center space-x-16">
                <div class="w-5/6 md:w-3/4 lg:w-2/3 xl:w-[500px] 2xl:w-[550px] mt-8 mx-auto px-16 py-8 rounded-lg">

                    <h2 class="text-center text-2xl font-bold tracking-wide text-gray-800">Sign Up</h2>
                    <p class="text-center text-sm text-gray-600 mt-2">Already have an account? <a href="#" class="text-blue-600 hover:text-blue-700 hover:underline" title="Sign In">Sign in here</a></p>

                    <form class="my-8 text-sm">
                        <div class="flex flex-col my-4">
                            <label for="name" class="text-gray-700">Name</label>
                            <input type="text" name="name" id="name" class="mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900" placeholder="Enter your name">
                        </div>

                        <div class="flex flex-col my-4">
                            <label for="email" class="text-gray-700">Email Address</label>
                            <input type="email" name="email" id="email" class="mt-2 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900" placeholder="Enter your email">
                        </div>
                        
                        <div class="flex flex-col my-4">
                            <label for="password" class="text-gray-700">Password</label>
                            <div x-data="{ show: false }" class="relative flex items-center mt-2">
                                <input :type=" show ? 'text': 'password' " name="password" id="password" class="flex-1 p-2 border pr-10 border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900" placeholder="Enter your password" type="password">
                                <button @click="show = !show" type="button" class="absolute right-2 bg-transparent flex items-center justify-center text-gray-700">
                                    <svg x-show="!show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>

                                    <svg x-show="show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="display: none;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                </button>
                            </div>
                        </div>

                        <div class="flex flex-col my-4">
                            <label for="password_confirmation" class="text-gray-700">Password Confirmation</label>
                            <div x-data="{ show: false }" class="relative flex items-center mt-2">
                                <input :type=" show ? 'text': 'password' " name="password_confirmation" id="password_confirmation" class="flex-1 p-2 pr-10 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 rounded text-sm text-gray-900" placeholder="Enter your password again" type="password">
                                <button @click="show = !show" type="button" class="absolute right-2 bg-transparent flex items-center justify-center text-gray-700">
                                    <svg x-show="!show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path></svg>

                                    <svg x-show="show" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="display: none;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                </button>
                            </div>
                        </div>

                        <div class="flex items-center">
                            <input type="checkbox" name="remember_me" id="remember_me" class="mr-2 focus:ring-0 rounded">
                            <label for="remember_me" class="text-gray-700">I accept the <a href="#" class="text-blue-600 hover:text-blue-700 hover:underline">terms</a> and <a href="#" class="text-blue-600 hover:text-blue-700 hover:underline">privacy policy</a></label>
                        </div>
                    
                        <div class="my-4 flex items-center justify-end space-x-4">
                            <button class="bg-blue-600 hover:bg-blue-700 rounded-lg px-8 py-2 text-gray-100 hover:shadow-xl transition duration-150 uppercase">Sign Up</button>
                        </div>
                    </form>
                </div>
                <div class="flex items-center justify-center">
                    <svg class="text-blue-600 w-5/6" style="transform: scale(-1,1);" xmlns="http://www.w3.org/2000/svg" data-name="Layer 1" width="582.544228" height="350.249375" viewBox="0 0 832.20604 500.35625" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M227.31663,699.06c-.05567-.24512-5.44-24.79785,5.55615-45.19043,10.99609-20.39166,34.46826-29.38477,34.7041-29.47363l1.07275-.40235.25342,1.11817c.05566.24511,5.43994,24.79785-5.55615,45.19043-10.99561,20.39166-34.46826,29.38476-34.7041,29.47363l-1.07325.40234Zm39.86181-72.33783c-4.70166,2.02246-23.25781,10.874-32.54492,28.09668-9.28809,17.22461-6.48584,37.59375-5.59229,42.63086,4.69971-2.01758,23.24854-10.85547,32.54493-28.09668C270.87375,652.1293,268.07248,631.76211,267.17844,626.72213Z" transform="translate(-183.89698 -199.82188)" fill="#f1f1f1"></path><path d="M254.94373,663.14907c-19.76056,11.88861-27.371,35.50269-27.371,35.50269s24.42779,4.3388,44.18835-7.54981,27.371-35.50268,27.371-35.50268S274.70429,651.26046,254.94373,663.14907Z" transform="translate(-183.89698 -199.82188)" fill="#f1f1f1"></path><path d="M554.19262,472.56441a10.83726,10.83726,0,0,0-10.47951-12.89681l-9.15082-23.01244-15.3409,2.15012,13.37918,32.31652a10.896,10.896,0,0,0,21.59205,1.44261Z" transform="translate(-183.89698 -199.82188)" fill="#9f616a"></path><path d="M525.92964,464.47855l-4.75346-11.3351-29.62149-56.38484,1.61062-104.33228.30923-.041c18.954-2.50423,31.77818,84.82857,32.315,88.54784l18.71553,64.00809,4.45518,14.10849Z" transform="translate(-183.89698 -199.82188)" fill="currentColor"></path><polygon points="296.518 484.658 310.92 484.657 317.771 429.106 296.515 429.107 296.518 484.658" fill="#9f616a"></polygon><path d="M476.741,679.77772l28.363-.00114h.00115a18.07611,18.07611,0,0,1,18.07514,18.07485v.58737l-46.43846.00172Z" transform="translate(-183.89698 -199.82188)" fill="#2f2e41"></path><polygon points="164.095 462.715 175.912 470.949 213.294 429.291 195.854 417.138 164.095 462.715" fill="#9f616a"></polygon><path d="M347.66667,656.57887l23.27053,16.21554.00094.00065a18.07611,18.07611,0,0,1,4.49515,25.16356l-.33583.4819L336.997,671.89089Z" transform="translate(-183.89698 -199.82188)" fill="#2f2e41"></path><path d="M472.49955,671.42229l-.62235-104.21007L462.81533,501.686,445.9204,559.31028l-.03285.04733-61.225,88.88515-23.82325-12.07048.13051-.31012c1.45591-3.46284,35.76216-84.7936,44.98333-84.7936a4.97985,4.97985,0,0,0,4.24236-1.86422c2.70645-3.614.50244-11.28284.47983-11.35983-2.63969-10.94588,3.99742-14.67362,5.3193-15.296l3.55555-73.397.36857.02543,96.38955,6.76108-4.04386,91.76589-8.69878,120.23153-.29881.03391Z" transform="translate(-183.89698 -199.82188)" fill="#2f2e41"></path><path d="M517.781,472.20177l-.41678-.03391L413.69966,463.8117l.25589-34.29989,5.07382-89.55836.02878-.06216,20.66277-44.85865,14.6473-6.63252,21.37023-1.12461.0521.01307,19.50283,4.83187,20.288,145.63873Z" transform="translate(-183.89698 -199.82188)" fill="currentColor"></path><circle cx="465.99537" cy="251.83011" r="27.29373" transform="translate(-247.58414 54.55847) rotate(-28.66324)" fill="#9f616a"></circle><path d="M438.54633,258.68144v-10.6343s-8.576-10.10035.85759-12.64464c0,0,2.57278-25.44285,24.87023-13.56952,0,0,30.87339-5.08857,27.443,12.72143,0,0,7.71835-4.64962,5.14556,7.22372L491.88689,260.904s2.40306-12.634-5.31529-14.33024l-4.288-2.54429s-12.00632,11.87334-30.0158-2.54428c0,0-7.71834-1.84217-6.86075,5.79069S438.54633,258.68144,438.54633,258.68144Z" transform="translate(-183.89698 -199.82188)" fill="#2f2e41"></path><path d="M463.15358,446.58748a10.83729,10.83729,0,0,0-12.62376-10.80688l-13.13193-20.99672-14.706,4.86818,18.96129,29.391a10.896,10.896,0,0,0,21.50042-2.45556Z" transform="translate(-183.89698 -199.82188)" fill="#9f616a"></path><path d="M429.23633,439.96884l-23.75756-48.2346.021-.11726c.09572-.53405,9.659-53.63372,16.97316-73.15156,7.36048-19.64146,17.43552-23.585,17.86078-23.74325l.21263-.07912,9.03379,8.66522-12.51394,83.527,13.489,40.28392Z" transform="translate(-183.89698 -199.82188)" fill="currentColor"></path><rect x="786.20604" width="46" height="46" fill="#f1f1f1"></rect><rect x="426.20604" y="179" width="46" height="46" fill="#f1f1f1"></rect><path d="M635.92184,404.66451H999.59653V220.55582H635.92184Z" transform="translate(-183.89698 -199.82188)" fill="#fff"></path><path d="M1002.59656,407.66458H632.92176V217.5557h369.6748Zm-363.6748-6h357.6748V223.5557H638.92176Z" transform="translate(-183.89698 -199.82188)" fill="#e5e5e5"></path><rect x="495.67778" y="85.31585" width="279.80647" height="9.27916" fill="#e5e5e5"></rect><rect x="495.67778" y="107.81893" width="279.80647" height="9.27916" fill="#e5e5e5"></rect><rect x="723.48425" y="141.04542" width="52" height="8.05267" fill="currentColor"></rect><path d="M565.897,700.13773h-381a1,1,0,1,1,0-2h381a1,1,0,0,1,0,2Z" transform="translate(-183.89698 -199.82188)" fill="#cbcbcb"></path></svg>
                </div>
            </div>
        </div>
</body>
</html>'''
    },{
    "html":'''<script defer src="https://unpkg.com/alpinejs@3.9.1/dist/cdn.min.js"></script>

<main class="flex min-h-screen w-full items-center justify-center bg-gray-100">
	<div x-data="{ open : false }" class="p-2 bg-white border shadow rounded w-96">
		<div x-show="!open" class="flex justify-between items-center">
			<div class="ml-2">Hafiz Haziq</div>
			<button type="button" class="btn bg-gray-200 hover:bg-gray-300 px-4 py-2 font-medium rounded"
                @click="open = !open">Edit</button>
		</div>

		<!-- container after clicked "EDIT" -->
		<div x-show="open" class="flex justify-between items-center">
			<input type="text" class="w-full bg-gray-100 rounded p-2 mr-4 border focus:outline-none focus:border-blue-500" value="Hafiz Haziq">

			<div class="flex justify-center items-center space-x-2">
				<button type="button" @click="open = false" class="btn bg-gray-200 hover:bg-gray-300 px-4 py-2 font-medium rounded">
                    Cancel
                </button>
				<button type="button" class="btn bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 font-medium rounded"
                    >
                    Save
                </button>
			</div>
		</div>
	</div>
</main>'''
    }
]
Footers=[
    {
    "html":'''<!-- This is an example component -->
<div class="max-w-2xl mx-auto">

	<footer class="p-4 bg-white rounded-lg shadow md:px-6 md:py-8 dark:bg-gray-800">
		<div class="sm:flex sm:items-center sm:justify-between">
			<a href="#" target="_blank" class="flex items-center mb-4 sm:mb-0">
				<img src="https://flowbite.com/docs/images/logo.svg" class="mr-4 h-8" alt="Flowbite Logo" />
				<span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
			</a>
			<ul class="flex flex-wrap items-center mb-6 sm:mb-0">
				<li>
					<a href="#" class="mr-4 text-sm text-gray-500 hover:underline md:mr-6 dark:text-gray-400">About</a>
				</li>
				<li>
					<a href="#" class="mr-4 text-sm text-gray-500 hover:underline md:mr-6 dark:text-gray-400">Privacy
						Policy</a>
				</li>
				<li>
					<a href="#"
						class="mr-4 text-sm text-gray-500 hover:underline md:mr-6 dark:text-gray-400">Licensing</a>
				</li>
				<li>
					<a href="#" class="text-sm text-gray-500 hover:underline dark:text-gray-400">Contact</a>
				</li>
			</ul>
		</div>
		<hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
		<span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2022 <a href="https://flowbite.com" target="_blank" class="hover:underline">Flowbite™</a>. All Rights Reserved.
    </span>
	</footer>

	<p class="mt-5">This footer component is part of a larger, open-source library of Tailwind CSS components. Learn
		more
		by going to the official <a class="text-blue-600 hover:underline"
			href="#" target="_blank">Flowbite Documentation</a>.
	</p>
</div>'''
    },{
    "html":'''<footer class="footer footer-center  w-full p-4 bg-gray-300 text-gray-800">
      <div class="text-center">
        <p>
          Copyright © 2022 -
          <a class="font-semibold" href="mailto:m.sohanemon@gmail.com"
            >SohanEmon</a
          >
        </p>
      </div>
    </footer>'''
    },{
    
    },{
    "html":'''<section class="bg-black">
       <div
            class="max-w-lg bg-black px-4 pt-24 py-8 mx-auto text-left md:max-w-none md:text-center"
          >
            <h1
              class="text-3xl font-extrabold leading-10 tracking-tight text-left text-white text-center sm:leading-none md:text-6xl text-4xl lg:text-7xl"
            >
              <span class="inline md:block">Join Us</span>
              <span
                class=" mt-2 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 via-emerald-400 to-green-500 md:inline-block"
              > We are<span class="bg-clip-text text-transparent bg-gradient-to-r from-teal-500 via-cyon-400 to-purple-300"> Hiring</span> </span>
            </h1>
            <div
              class="mx-auto rounded-lg font-black mt-5 text-zinc-400 md:mt-12 md:max-w-lg text-center lg:text-lg"
            >
              <button class="bg-tkb border text-sm text-white py-3 px-7 rounded-full" onClick={signInNow}>
              Join Sahilnetic
              </button>
            </div>
          </div>
  </section>
  
<hr class="text-white mx-5" />
  <footer class="bg-black pb-5">
  <div class="max-w-screen-xl px-4 pt-8 mx-auto sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center sm:justify-between">
      <div class="flex justify-center text-teal-300 sm:justify-start">
     <img class="rounded-full" src="https://sahilnetic.xyz/evilcat.png" width="40" height="40" />
      </div>

      <p class="mt-4 text-sm text-center text-gray-400 lg:text-right lg:mt-0">
        T&C &nbsp; Career &nbsp; Privacy & Policy &nbsp; Developers
      </p>
    </div>
  </div>
</footer>'''
    },{
    "html":'''<!-- This is an example component -->
<div class="max-w-2xl mx-auto">

	<footer class="p-4 bg-white sm:p-6 dark:bg-gray-800">
		<div class="md:flex md:justify-between">
			<div class="mb-6 md:mb-0">
				<a href="#" target="_blank" class="flex items-center">
					<img src="https://flowbite.com/docs/images/logo.svg" class="mr-4 h-10" alt="FlowBite Logo">
					<span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
				</a>
			</div>
			<div class="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3">
				<div>
					<h3 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Resources</h3>
					<ul>
						<li class="mb-4">
							<a href="#" target="_blank"
								class="text-gray-600 hover:underline dark:text-gray-400">Flowbite</a>
						</li>
						<li>
							<a href="#" target="_blank" rel="nofollow"
								class="text-gray-600 hover:underline dark:text-gray-400">Tailwind CSS</a>
						</li>
					</ul>
				</div>
				<div>
					<h3 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Follow us</h3>
					<ul>
						<li class="mb-4">
							<a href="#" target="_blank"
								class="text-gray-600 hover:underline dark:text-gray-400">Github</a>
						</li>
						<li>
							<a href="#" target="_blank"
								class="text-gray-600 hover:underline dark:text-gray-400">Discord</a>
						</li>
					</ul>
				</div>
				<div>
					<h3 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Legal</h3>
					<ul>
						<li class="mb-4">
							<a href="#" target="_blank" class="text-gray-600 hover:underline dark:text-gray-400">Privacy
								Policy</a>
						</li>
						<li>
							<a href="#" target="_blank" class="text-gray-600 hover:underline dark:text-gray-400">Terms
								&amp; Conditions</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8">
		<div class="sm:flex sm:items-center sm:justify-between">
			<span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2022 <a href="https://flowbite.com" target="_blank" class="hover:underline">Flowbite™</a>. All Rights Reserved.
</span>
			<div class="flex mt-4 space-x-6 sm:justify-center sm:mt-0">
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path
							d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84">
						</path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
				<a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
					<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path fill-rule="evenodd"
							d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z"
							clip-rule="evenodd"></path>
					</svg>
				</a>
			</div>
		</div>
	</footer>

	<p class="mt-5">This footer component is part of a larger, open-source library of Tailwind CSS components. Learn
		more
		by going to the official <a class="text-blue-600 hover:underline"
			href="#" target="_blank">Flowbite Documentation</a>.
	</p>
</div>'''
    },{
    "html":'''<footer class="relative py-20 flex flex-col items-center bg-cyan-900 overflow-hidden md:py-40">
    <div class="relative z-[1] container m-auto px-6 md:px-12">
        <div class="m-auto md:w-10/12 lg:w-8/12 xl:w-6/12">
            <div class="flex flex-wrap items-center justify-between md:flex-nowrap">
                <div class="w-full space-x-12 flex justify-center text-gray-300 sm:w-7/12 md:justify-start">
                    <ul class="list-disc list-inside space-y-8">
                        <li><a href="#" class="hover:text-sky-400 transition">Home</a></li>

                        <li><a href="#" class="hover:text-sky-400 transition">About</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Guide</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Blocks</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Contact</a></li>
                        <li><a href="#" class="hover:text-sky-400 transition">Terms of Use</a></li>
                    </ul>

                    <ul role="list" class="space-y-8">
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                                </svg>
                                <span>Github</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                                </svg>
                                <span>Twitter</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                                </svg>
                                <span>YouTube</span>
                            </a>
                        </li>

                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
<path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
                                </svg>
                                <span>Facebook</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
                                    <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8zm4.95 0c0 2.34-1.01 4.236-2.256 4.236-1.246 0-2.256-1.897-2.256-4.236 0-2.34 1.01-4.236 2.256-4.236 1.246 0 2.256 1.897 2.256 4.236zM16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795z"/>
                                </svg>
                                <span>Medium</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="5" viewBox="0 0 16 16">
                                    <path d="M8 0a8 8 0 0 0-2.915 15.452c-.07-.633-.134-1.606.027-2.297.146-.625.938-3.977.938-3.977s-.239-.479-.239-1.187c0-1.113.645-1.943 1.448-1.943.682 0 1.012.512 1.012 1.127 0 .686-.437 1.712-.663 2.663-.188.796.4 1.446 1.185 1.446 1.422 0 2.515-1.5 2.515-3.664 0-1.915-1.377-3.254-3.342-3.254-2.276 0-3.612 1.707-3.612 3.471 0 .688.265 1.425.595 1.826a.24.24 0 0 1 .056.23c-.061.252-.196.796-.222.907-.035.146-.116.177-.268.107-1-.465-1.624-1.926-1.624-3.1 0-2.523 1.834-4.84 5.286-4.84 2.775 0 4.932 1.977 4.932 4.62 0 2.757-1.739 4.976-4.151 4.976-.811 0-1.573-.421-1.834-.919l-.498 1.902c-.181.695-.669 1.566-.995 2.097A8 8 0 1 0 8 0z"/>
                                </svg>
                                <span>Pintrest</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <img class="w-5 h-5" src="https://c5.patreon.com/external/favicon/favicon.ico?v=69kMELnXkB" alt="patreon icon">
                                <span>Patreon</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center space-x-3 hover:text-sky-400 transition">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-5" viewBox="0 0 16 16">
                                    <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"/>
                                </svg>
                                <span>Instagram</span>
                            </a>
                        </li>
                        
                    </ul>
                </div>
                <div class="w-10/12 m-auto  mt-16 space-y-6 text-center sm:text-left sm:w-5/12 sm:mt-auto">
                    <span class="block text-gray-300">We change the way UI components librairies are used</span>

                    <span class="block text-gray-300">Tailus Blocks &copy; 2021</span>

                    <span class="flex justify-between text-white"> 
                        <a href="#" class="font-semibold">Terms of Use </a>
                        <a href="#" class="font-semibold"> Privacy Policy</a> 
                    </span>

                    <span class="block text-gray-300">Need help? <a href="#" class="font-semibold text-white"> Contact Us</a></span>
                </div>
            </div>
        </div>
    </div>
    <div aria-hidden="true" class="absolute h-full inset-0 flex items-center">
        <div aria-hidden="true" class="bg-layers bg-scale w-56 h-56 m-auto blur-xl bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-600 rounded-full md:w-[30rem] md:h-[30rem] md:blur-3xl"></div>
    </div>
    <div aria-hidden="true" class="absolute inset-0 w-full h-full bg-[#020314] opacity-80"></div>
</footer>

<!--

    Add to your stylesheet

.bg-layers {
    -webkit-animation: filter-animation 4s infinite;
    animation: filter-animation 4s infinite;
}

.bg-scale {
    -webkit-animation: filter-animation 8s infinite;
    animation: filter-scale 8s infinite;
}
  
@-webkit-keyframes filter-animation {
    0% {
      -webkit-filter: hue-rotate(0deg);
    }
    50% {
      -webkit-filter: hue-rotate(45deg);
    }
    
    100% {
      -webkit-filter: hue-rotate(0deg);
    }
}
  
@keyframes filter-animation {
    0% {
      filter: hue-rotate(0deg);
    }
    50% {
      filter: hue-rotate(45deg);
    }
    100% {
      filter: hue-rotate(0deg);
    }
}

@keyframes filter-scale {
    0% {
      transform:scale(1);
    }
    50% {
      transform:scale(1.4);
    }
    100% {
        transform:scale(.8);
    }
}
-->'''
    },{
    "html":''''''
    }
]