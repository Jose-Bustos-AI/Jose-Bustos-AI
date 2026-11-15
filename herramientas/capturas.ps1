$d = "C:\Users\usuario\AppData\Local\Temp\claude\49bef18d482478ee\5bae3f2c-87e1-4f3f-848a-e41d3497cc33\scratchpad\gh"
$ch = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$sitios = [ordered]@{
  ahl          = "https://www.aihumanslab.com/"
  c2m          = "https://www.click2model.es/"
  gastro       = "https://nuevo.innovagastro.es/demo"
  lumiere      = "https://lumiere.innovapymes.ai/"
  companions   = "https://companions.innovapymes.ai/avatars/"
  nordauto     = "https://nordauto-markina.vercel.app"
  pilates      = "https://pilatessanse-demo.vercel.app"
  glousie      = "https://web-demo-glousie-murcia.vercel.app"
  reformas     = "https://web-demo-maria-candida-aleman-hita.vercel.app"
  ecofresh     = "https://eco-fresh-gdrn.vercel.app"
  estefania    = "https://estefania-plaza-demo.vercel.app"
  mariamartin  = "https://maria-martin-demo.vercel.app"
  ambinature   = "https://ambinature-andorra.vercel.app"
  gastrovisual = "https://gastrovisual-innovapymes-projects.vercel.app"
  tunel        = "https://dania-tunel.vercel.app"
  barbara      = "https://barbara-marrero-psicologia.vercel.app"
}
foreach ($n in $sitios.Keys) {
  $out = "$d\cap\$n.png"
  if (Test-Path $out) { Remove-Item $out -Force -Confirm:$false }
  $p = Start-Process -FilePath $ch -ArgumentList @("--headless=new","--no-first-run","--hide-scrollbars","--enable-unsafe-swiftshader","--user-data-dir=`"$d\perfil-chrome`"","--window-size=1280,800","--virtual-time-budget=12000","--screenshot=`"$out`"",$sitios[$n]) -PassThru -NoNewWindow -RedirectStandardError "$d\err.txt"
  if (-not $p.WaitForExit(70000)) { try { $p.Kill() } catch {} }
  if (Test-Path $out) { "{0}: {1} KB" -f $n, [int]((Get-Item $out).Length / 1024) } else { "{0}: sin captura" -f $n }
}
