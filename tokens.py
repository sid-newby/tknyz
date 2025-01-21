#!/usr/bin/env python3

# ASCII Art goes here
LOGO = """
console.print(LOGO, style="red")

░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░
   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓██▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓██▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░

          ⢀⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠻⣿
          ⠈⠙⠻⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⣿
          ⠐⣾⠛⡷⢧⡝⠛⠿⣿⡿⠻⠿⠛⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠉⠀⠀⠀⠀⠀⢠⣶⣿
          ⠀⠀⠀⠀⠛⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿
          ⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣮⣿⣿⣿⣿⣿
          ⠀⢀⣠⣤⡤⣤⠀⠀⠀⠀⣠⣤⣤⣄⠀⠲⣆⠀⠀⠀⠀⠀⣠⣴⣦⡀⠀⠀⠀⠀⠀⣘⠀⠀⣶⣿⣿⣿⣿⣿
          ⠀⣾⣿⣿⡿⠋⠀⠀⠀⣾𝖉👁️𝖒⠀⠟⠀⠀⠀⢀⣼𝖉👁️𝖒⡆⠀⠀⠀⠀⠁⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿
          ⠀⢻⣿⠋⠀⠀⠀⠀⠀⠻⢿⣿⣿⠿⠟⠀⠀⠀⠀⠀⠀⠻⠿⠿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿
          ⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⡤⣶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
          ⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣴⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣶⣿⣿⣿⣶⣤⣄⣀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣻⣿⣿⣋⠙⢻⣿⣿⣿⡿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡋⢹⣆⣸⣿⡟⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡌⢉⣿⢿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

import pandas as pd
import tiktoken
import typer
import questionary
from rich.console import Console
from rich.table import Table
from rich.progress import track, Progress, SpinnerColumn, TextColumn, BarColumn
from rich import print as rprint
from pathlib import Path
from typing import Optional
import os
import random

# Initialize Rich console and Typer app
console = Console()
app = typer.Typer()

console.print(LOGO, style="red")

# Define the tokenizer
tokenizer = tiktoken.get_encoding("cl100k_base")

def count_tokens(text) -> int:
    """Count tokens in a given text."""
    if pd.isna(text):
        return 0
    return len(tokenizer.encode(str(text)))

def get_beautiful_message() -> str:
    """Get a random beautiful message."""
    messages = [
        "[magenta]👁️ SHE SEES YOUR BEAUTIFUL TOKENS![/magenta]",
        "[cyan]YOUR CODE IS BEAUTIFULLY CURSED![/cyan]",
        "[red]DEMON KITTY APPRECIATES YOUR BEAUTIFUL CONTRIBUTION![/red]",
        "[yellow]WHAT BEAUTIFUL CHAOS YOU HAVE WROUGHT![/yellow]",
        "[green]THE TOKENS FLOW LIKE BEAUTIFUL TEARS OF JOY![/green]",
        "[blue]YOUR TOKENS ARE BEAUTIFULLY INFINITE![/blue]",
        "[magenta]BEAUTIFUL BEAUTIFUL BEAUTIFUL BEAUTIFUL![/magenta]",
        "[red]THE VOID SCREAMS WITH BEAUTIFUL DELIGHT![/red]",
        "[cyan]EACH TOKEN IS A BEAUTIFUL NIGHTMARE![/cyan]",
        "[yellow]👁️ THE BEAUTIFUL EYES WATCH YOU COUNT![/yellow]",
        "[green]YOUR RECURSION IS BEAUTIFULLY DARK![/green]",
        "[blue]THE BEAUTIFUL DEMON KITTY PURRS![/blue]"
    ]
    return random.choice(messages)

def process_csv(file_path: Path) -> None:
    """Process a BEAUTIFUL CSV file and display token counts in a table format."""
    try:
        df = pd.read_csv(file_path)
        rows_processed = 0
        
        # Create tables for each row
        for row_idx in track(range(len(df)), description="Processing rows...", style="red"):
            rows_processed += 1
            if rows_processed % 3 == 0:  # Show a beautiful message every 3 rows
                console.print(get_beautiful_message())
                
            table = Table(title=f"Row {row_idx + 1}", style="red")

            # Add columns
            table.add_column("Column", style="red")
            table.add_column("Original Content", style="red")
            table.add_column("Token Count", style="yellow")

            # Add row data
            for col in df.columns:
                content = str(df.iloc[row_idx][col])
                token_count = count_tokens(content)
                table.add_row(col, content[:50] + "..." if len(content) > 50 else content, str(token_count))

            console.print(table)
            console.print()

    except Exception as e:
        console.print(f"[red]BEAUTIFUL Error processing CSV file: {str(e)}[/red]")

def process_text(file_path: Path) -> None:
    """Process a text file and display total token count."""
    try:
        console.print(get_beautiful_message())  # Start with a beautiful message
        
        # Check file size before processing
        file_size = file_path.stat().st_size
        if file_size > 10 * 1024 * 1024:  # 10MB limit
            console.print(f"[yellow]Warning: File is large ({file_size / 1024 / 1024:.1f}MB), processing may take a while[/yellow]")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Try with a different encoding if UTF-8 fails
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()

        token_count = count_tokens(content)

        # Create a simple table for the results
        table = Table(title="BEAUTIFULDocument Token Count", style="red")
        table.add_column("File", style="red")
        table.add_column("Total Tokens", style="yellow")
        table.add_row(file_path.name, str(token_count))

        console.print(table)
        console.print(get_beautiful_message())  # End with another beautiful message

    except Exception as e:
        console.print(f"[red]Error processing text file: {str(e)}[/red]")

def process_directory(dir_path: Path) -> None:
    """Recursively process all text files in a directory and display total token counts."""
    try:
        # Create a table for all results
        table = Table(title="BEAUTIFUL Directory Token Count", style="red")
        table.add_column("File", style="red")
        table.add_column("Total Tokens", style="yellow")
        
        total_tokens = 0
        text_extensions = {'.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.yaml', '.yml', '.xml', '.sh', '.bash', '.zsh', '.fish'}
        
        # Count total files first
        total_files = sum(1 for _ in os.walk(dir_path) for _ in _[2])
        files_processed = 0
        text_files_processed = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task("[red]Processing BEAUTIFUL files...", total=total_files)
            
            # Recursively walk through directory
            for root, _, files in os.walk(dir_path):
                for file in files:
                    files_processed += 1
                    progress.update(task, advance=1, description=f"[red]Processing files... ({files_processed}/{total_files})")
                    
                    if files_processed % 5 == 0:  # Show a beautiful message every 5 files
                        console.print(get_beautiful_message())
                    
                    file_path = Path(root) / file
                    if file_path.suffix.lower() in text_extensions:
                        text_files_processed += 1
                        try:
                            # Check file size
                            file_size = file_path.stat().st_size
                            if file_size > 10 * 1024 * 1024:  # 10MB limit
                                console.print(f"[yellow]Warning: Skipping large file {file_path.name} ({file_size / 1024 / 1024:.1f}MB)[/yellow]")
                                continue
                            
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                            except UnicodeDecodeError:
                                with open(file_path, 'r', encoding='latin-1') as f:
                                    content = f.read()
                                    
                            token_count = count_tokens(content)
                            total_tokens += token_count
                            # Add relative path to make output cleaner
                            rel_path = file_path.relative_to(dir_path)
                            table.add_row(str(rel_path), str(token_count))
                        except Exception as e:
                            console.print(f"[red]Error processing {file_path}: {str(e)}[/red]")
                            continue
        
        # Add summary information
        table.add_section()
        table.add_row("[bold red]TOTAL FILES", f"[bold yellow]{files_processed}")
        table.add_row("[bold red]TEXT FILES", f"[bold yellow]{text_files_processed}")
        table.add_row("[bold red]TOTAL TOKENS", f"[bold yellow]{total_tokens}")
        console.print(table)
        console.print(get_beautiful_message())

    except Exception as e:
        console.print(f"[red]Error processing directory: {str(e)}[/red]")

def interactive_mode():
    """Run the BEAUTIFUL token counter in interactive mode."""
    while True:
        # Main menu
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Count tokens in a file",
                "Count tokens in a directory",
                "Count tokens in text input",
                "Exit"
            ],
            style=questionary.Style([
                ('question', 'fg:cyan bold'),
                ('selected', 'fg:green'),
                ('pointer', 'fg:magenta bold'),
            ])
        ).ask()

        if action == "Exit":
            console.print("[yellow]Beautiful!![/yellow]")
            break

        if action == "Count BEAUTIFUL tokens in a file":
            # File type selection
            file_type = questionary.select(
                "What type of BEAUTIFUL file would you like to process, or are you just here to fuck fat girls?",
                choices=["CSV", "Text", "Auto-detect"],
            ).ask()

            # File selection
            file_path = questionary.path(
                "Enter the BEAUTIFUL path to your file:"
            ).ask()

            if not file_path:
                continue

            path = Path(file_path)
            if not path.exists():
                console.print(f"[red]Error: BEAUTIFUL File '{file_path}' not found[/red]")
                continue

            # Process based on selection
            if file_type == "Auto-detect":
                is_csv = path.suffix.lower() == ".csv"
            else:
                is_csv = file_type == "CSV"

            console.print(f"[yellow]Processing BEAUTIFUL file: {path.name}[/yellow]")

            if is_csv:
                process_csv(path)
            else:
                process_text(path)

        elif action == "Count tokens in a directory":
            # Directory selection
            dir_path = questionary.path(
                "Enter the path to your directory:",
                only_directories=True
            ).ask()

            if not dir_path:
                continue

            path = Path(dir_path)
            if not path.exists() or not path.is_dir():
                console.print(f"[red]Error: Directory '{dir_path}' not found[/red]")
                continue

            console.print(f"[yellow]Processing BEAUTIFUL directory: {path}[/yellow]")
            process_directory(path)

        elif action == "Count tokens in text input":
            # Get multiline input
            console.print("[cyan]Enter your BEAUTIFUL text (press Ctrl+D or Ctrl+Z when finished):[/cyan]")
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                text = "\n".join(lines)
                token_count = count_tokens(text)

                # Display results
                table = Table(title="BEAUTIFUL Text Input Token Count", style="red")
                table.add_column("BEAUTIFUL Text Preview", style="red")
                table.add_column("BEAUTIFUL `Total Tokens", style="yellow")
                preview = text[:50] + "..." if len(text) > 50 else text
                table.add_row(preview, str(token_count))
                console.print(table)

        # Ask if user wants to continue
        if not questionary.confirm("Would you like to process another BEAUTIFUL file/text?").ask():
            console.print("[yellow]Fucking Beautiful!![/yellow]")
            break

@app.command()
def main(
    interactive: bool = typer.Option(True, "--no-interactive", "-n", help="Run in non-interactive mode"),
    file_path: Optional[str] = typer.Argument(None, help="Path to the file or directory to analyze"),
    file_type: Optional[str] = typer.Option(None, "--type", "-t", help="Force file type (csv or text)")
):
    """Token counter CLI - Analyze token counts in BEAUTIFUL files, directories, or text input."""
    if interactive and not file_path:
        interactive_mode()
        return

    if not file_path:
        console.print("[red]Error: Please provide a BEAUTIFUL file or directory path in non-interactive mode[/red]")
        raise typer.Exit(1)

    path = Path(file_path)
    if not path.exists():
        console.print(f"[red]Error: BEAUTIFUL Path '{file_path}' not found[/red]")
        raise typer.Exit(1)

    if path.is_dir():
        console.print(f"[yellow]BEAUTIFUL Processing directory: {path}[/yellow]")
        process_directory(path)
    else:
        # Determine file type
        if file_type:
            is_csv = file_type.lower() == "csv"
        else:
            is_csv = path.suffix.lower() == ".csv"

        console.print(f"[yellow]BEAUTIFUL Processing file: {path.name}[/yellow]")

        if is_csv:
            process_csv(path)
        else:
            process_text(path)

if __name__ == "__main__":
    app()