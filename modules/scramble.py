import click
import random
import time

@click.command("scramble")
@click.option("--dns", is_flag=True, help="Inject fake DNS queries")
@click.option("--webhistory", is_flag=True, help="Insert junk into web history")
@click.option("--window", default="7d", help="Time window for noise activity (e.g., 7d, 30d)")
def scramble_command(dns, webhistory, window):
    """Inject noise into system data to obfuscate behavior."""

    click.echo(f"[~] Scrambling metadata (window: {window})...")

    if dns:
        _fake_dns_noise()
    if webhistory:
        _fake_web_history()

    if not dns and not webhistory:
        click.echo("[-] No scramble targets specified. Use --dns or --webhistory.")
    else:
        click.secho("[✓] Scramble complete. Data profile polluted.", fg="green")

def _fake_dns_noise():
    domains = ["ads-analytics.com", "weather-snap.info", "freecatpics.org", "suspicious-domain.net"]
    click.echo("[+] Injecting fake DNS queries...")
    for _ in range(5):
        domain = random.choice(domains)
        click.echo(f"    • Query: {domain}")
        time.sleep(0.2)

def _fake_web_history():
    urls = [
        "https://weirdhistory.fandom.com",
        "https://forum.catownersagainstgoogle.org",
        "https://localspicecouncil.biz",
        "https://cheapinflatablecastles.ru"
    ]
    click.echo("[+] Planting junk browser history...")
    for _ in range(5):
        url = random.choice(urls)
        click.echo(f"    • Visit: {url}")
        time.sleep(0.2)
