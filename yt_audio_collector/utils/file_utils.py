import json
import os
from pathlib import Path
from typing import Any, Union


def resolve_path(file_path: Union[str, Path]) -> Path:

    """
    Check if the given file path exists and return a Path object if it does.
    

    Parameters:
    ----------- 
    file_path: `Union[str, Path]`
        The path of the file to check.
        
    Exceptions:
    -----------           
    FileNotFoundError:             
        If the file path does not exist.

    Return:
    -------                 
    Path         
        The Path object of the file path.  
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found")
    return file_path


def load_json(file_path: Union[str, Path]) -> Any:
    """
    Load data from a JSON file.
    

    Parameters:
    ----------- 
    file_path: `Union[str, Path]`
        The path of the JSON file.
        
    Return:
    -------                 
    Any    
        A dictionary with the data in the file.  
    """
    file_path = resolve_path(file_path)

    with open(file_path, "r", encoding="utf-8") as file_reader:
        try:
            json_data = json.load(file_reader)
        except json.decoder.JSONDecodeError:
            json_data = {}

    return json_data


def create_dir(dir_path: Union[str, Path]) -> Path:
    """
    Create a directory with the given path.

    Parameters:
    ----------- 
    dir_path: `Union[str, Path]`
        The path of the directory to create.

    Return:
    -------                 
    Path         
        The created directory path.  
    """
    if isinstance(dir_path, str):
        dir_path = Path(dir_path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path

