// Blank string to append HTML to below
bubbles_html = '';

// Add specified number of bubbles
for (var i = 0; i <= 100; i++){
    // Determine bubble CSS properties using random values
    size = Math.floor(Math.random() * 80) + 10;
    position_top = Math.floor(Math.random() * 100);
    position_left = Math.floor(Math.random() * 100);
    opacity = Math.random() / 2;
    blur = Math.random() / 5;
    // Create bubble and add it to bubbles html
    bubbles_html += `<span id="bubble-${i}" style="z-index: 0; width: ${size}px; height: ${size}px; top: ${position_top}vh; left: ${position_left}vw; opacity: ${opacity}; filter: blur(${blur}em);"></span>`;
}

// Inject the bubbles HTML
$('#bubbles').html(bubbles_html);
